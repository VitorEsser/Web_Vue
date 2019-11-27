<template>
  <v-container>
      <div v-for="pet in pets" v-bind:key="pet.id">
        <p>{{pet.name}}</p>
        <p>{{pet.vaccine}}</p>
        <p>{{pet.description}}</p>
        <p>{{pet.category_name}}</p>
        
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deletePet(pet)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editPet(pet)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
      </div>
      <CreatePets @updatePets="all"></CreatePets>
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreatePets from "./Create";

export default {
  name: "ListPets",
  data() {
    return {
      pets: [],
    };
  },
  components: {
    CreatePets: CreatePets,
  },
  created() {
    this.all();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/pets/"
        })
        .then(response => {
          this.pets = response.data
          console.log(response)
        });
    },
    deletePet(pet) {
      if (confirm("Excluir " + pet.name)) {
        axios
          .delete(`http://localhost:8000/api/pets/${pet.id}`, {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          })
          .then(response => {
            this.all()
            console.log(response)
          });
      }
    },
    editPet(pet) {
      router.push(`/pets/edit/${pet.id}`)
    }
  }
};
</script>