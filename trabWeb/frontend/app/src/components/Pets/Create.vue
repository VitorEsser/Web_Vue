<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-card-text>
          <v-fab-transition>
            <v-btn primary v-on="on" dark relative fixed bottom right fab>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </template>

      <v-card>
        <v-card-title>
          <span class="headline">Adicionar Pets</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="pet.name" label="Nome*" hint="Nome do Pet" required></v-text-field>
              </v-col>
              <v-row class="form-group" v-for="(input,k) in petvaccines" :key="k">
                
              <v-col cols="7">
                <v-select
                  :items = "vaccines"
                  item-value = "id"
                  item-text = "name"
                  label = "Vacinas"
                  attach
                  single-line
                  v-model = "input.vaccine"
                >
                </v-select>
              </v-col>
              <v-col cols="1">
                    <v-icon 
                      @click="addvaccine(k)"
                    >mdi-plus</v-icon>
                    <v-icon 
                      @click="removevaccine(k)"
                      v-show="k || ( !k && petvaccines.length > 1)">
                       mdi-minus
                    </v-icon>
              </v-col>
              </v-row>
              <v-col cols="12">
                <v-text-field v-model="pet.description" label="Descrição*" type="text" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-select
                  :items = "categories"
                  item-value = "id"
                  item-text = "name"
                  label = "Categoria"
                  attach
                  v-model = "pet.category"
                >
                </v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*informações obrigatórias</small>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="dialog = false">Fechar</v-btn>
          <v-btn color="blue darken-1" text @click="add()">Salvar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
import axios from "axios"
export default {
  name: "CreatePet",
  data() {
    return {
      dialog: false,
      categories: [],
      vaccines: [],
      pet: {},
      petvaccines: [{
        vaccine: "",
      }],
    };
  },
  created() {
    this.getCategories()
    this.getVaccines()
  },
  methods: {
    addvaccine(index) {
      this.petvaccines.push({ name: ''});
    },
    removevaccine(index) {
      this.petvaccines.splice(index, 1);
    },
    getCategories() {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/categories/"
      })
      .then(response => {
        this.categories = response.data
        console.log(response)
      });
    },
    getVaccines() {
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
    add() {
      this.pet.vaccines = this.petvaccines
      axios
        .post("http://localhost:8000/api/pets/add/",
          this.pet, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(response => {
          this.dialog = false
          this.$emit('updatePets')
          this.log.console(response)
        });
    }
  }
};
</script>
