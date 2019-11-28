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
          <span class="headline">Adicionar Vacinas</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="vaccines.name" label="Nome*" hint="Nome da Vacina" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="vaccines.description" label="Descrição*" type="text" required></v-text-field>
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
  name: "CreateVaccine",
  data() {
    return {
      dialog: false,
      vaccines: [],
    };
  
  },
  methods: {
    addvaccine(index) {
      this.vaccines.push({ name: ''});
    },
    removevaccine(index) {
      this.vaccines.splice(index, 1);
    },
    add() {
      this.vaccines = this.vaccines
      axios
        .post("http://localhost:8000/api/vaccines/add/",
          this.vaccine, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(response => {
          this.dialog = false
          this.$emit('updateVaccines')
        });
    }
  }
}
</script>
