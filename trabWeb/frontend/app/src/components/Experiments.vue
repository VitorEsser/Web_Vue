<template>
  <section>
    <h1>Teste</h1>
    <h3>{{texto}}</h3>
    <v-select
      :items = "items"
      item-value = "id"
      item-text = "name"
      label = "Categorias de Pets"
      attach
      multiple
      chips
      v-model = "escolha"
    >
    </v-select>
    <h3>Minha escolha</h3>
    {{escolha}}
  </section>
</template>

<script>
import axios from "axios"
export default {
    name: "Experiments",
    data () {
      return  {
        texto: "Exemplo de Select",
        items: [],
        escolha: "",
      }
    },
    created() {
      this.getCategories()
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
}
</script>

<style>

</style>