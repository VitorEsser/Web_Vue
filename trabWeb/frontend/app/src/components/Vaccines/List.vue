<template>
  <v-container>
      <div v-for="vaccine in vaccines" v-bind:key="vaccine.id">
        <br>
        <p><strong>Nome:</strong> {{vaccine.name}}</p>
        <p><strong>Descrição:</strong> <br>{{vaccine.description}}</p>
        
        <v-divider></v-divider>
        <br>
      </div>
      <CreateVaccines @updateVaccines="all" />
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateVaccines from "./Create";


export default {
  name: "ListVaccines",
  data() {
    return {
      vaccines: [],
    };
  },
  components: {
    CreateVaccines,
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
          url: "/api/vaccines/"
        })
        .then(response => {
          this.vaccines = response.data
          console.log(response)
        });
    },
  }
};
</script>