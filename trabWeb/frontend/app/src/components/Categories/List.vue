<template>
  <v-container>
    <div>
        <h1 id="h1-category">Categoria dos Pets: </h1>
        <v-select
        :items = "items"
        item-value = "id"
        item-text = "name"
        label = "Categorias de Pets"
        attach
        multiple
        chips
        >
        </v-select>
    </div>
      <CreateCategories @updateCategories="all" />
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateCategories from "./Create";


export default {
  name: "ListCategories",
  data() {
    return {
      vaccines: [],
      items: [],
    };
  },
  components: {
    CreateCategories,
  },
  created() {
    this.getCategories();
  },
  methods: {
    getCategories() {
        axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/categories/"
        })
        .then(response => {
          this.items = response.data
          console.log(response)
        });
    }
  }
};
</script>

<style>
  #h1-category{
    margin-top: 30%;
  }
</style>