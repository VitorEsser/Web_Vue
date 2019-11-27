<template>
  <v-container>
    <h1>Editar Pet</h1>
    <form>
      <v-text-field
        v-model="pet.name"
        :error-messages="nameErrors"
        :counter="100"
        label="Nome"
        required
        @input="$v.pet.name.$touch()"
        @blur="$v.pet.name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="pet.vaccine"
        :error-messages="authorErrors"
        label="Vacina"
        required
        @input="$v.pet.vaccine.$touch()"
        @blur="$v.pet.vaccine.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="pet.description"
        :error-messages="descriptionErrors"
        label="Descrição"
        required
        @input="$v.pet.description.$touch()"
        @blur="$v.pet.description.$touch()"
      ></v-text-field>
      <v-btn class="mr-4" @click="submit">Enviar</v-btn>
      <v-btn @click="clear">Limpar</v-btn>
    </form>
  </v-container>
</template>

<script>
import axios from "axios"
import route from "@/router/"
import { validationMixin } from 'vuelidate'

import { required, maxLength } from 'vuelidate/lib/validators'

export default {
  name: 'EditPet',
  created () {
    this.getPetInfo()
  },
  mixins: [validationMixin],

  validations: {
    pet: {
      name: {
        maxLength: maxLength(100),
        required
      },
      description: {
        required
      },
      vaccine: {
        required
      },
    }
  },

  data () {
    return {
      name: "",
      vaccine: "",
      description: "",
      pet: {}
    }
  },
  computed: {
    nameErrors () {
      const errors = []
      if (!this.$v.pet.name.$dirty) return errors
      !this.$v.pet.name.maxLength && errors.push('Nome deve ter até 100 caracteres.')
      !this.$v.pet.name.required && errors.push('Nome é obrigatório.')
      return errors
    },
    vaccineErrors () {
      const errors = []
      if (!this.$v.pet.vaccine.$dirty) return errors
      !this.$v.pet.vaccine.required && errors.push('Vacina é obrigatório.')
      return errors
    },
    descriptionErrors () {
      const errors = []
      if (!this.$v.pet.description.$dirty) return errors
      !this.$v.pet.description.required && errors.push('Descrição é obrigatório.')
      return errors
    },
  },
  methods: {
    getPetInfo() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: `/api/pets/get/${this.$route.params.id}/`
        })
        .then(res => {
          this.pet = res.data
          console.log(res)
        });
    },
    submit () {
      axios
        .put(
          `http://localhost:8000/api/pets/edit/${this.$route.params.id}/`,
          this.pet, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(res => {
          route.push('/pets/')
          console.log(res)
        });
    },
    clear () {
      route.push('/pets/')
    },
  }
}
</script>