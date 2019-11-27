<template>
  <v-card-text>
    <v-form ref="form">
      <v-text-field label="Usuário"
        v-model="credentials.username"
        name="login" 
        prepend-icon="person" 
        type="text"
        :rules="rules.username"
        required
      ></v-text-field>

      <v-text-field label="Senha"
        v-model="credentials.password"
        id="password"
        name="password"
        prepend-icon="lock"
        type="password"
        :rules="rules.password"
        required
      ></v-text-field>
    </v-form>
  </v-card-text>
</template>

<script>
export default {
  data() {
    return {
      credentials: {},
      rules: {
        username: [v => !!v || "Usuário é obrigatório."],
        password: [
          v => !!v || "Senha é obrigatória.",
          v => (v && v.length > 2) || "A senha deve ser maior que 2 caracteres."
        ]
    }
    }
  },
  watch: {
    credentials: {
      deep: true,
      handler() {
        this.$emit('fillCredentials', this.credentials)
      }
    }
  },
  methods: {
    touch() {
      this.$v.form.$touch()
    }
  }
}
</script>

<style>

</style>