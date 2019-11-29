<template>
  <section class="container">
    <h1 align="center">BEM VINDO AO </h1> 
    <h2 align="center">SOS - CLÍNICA DE VACINAÇÃO!!</h2>
  </section>
</template>

<script>
import router from "../router";

export default {
  name: "Index",
  data() {
    return {
      authenticated: false
    };
  },
  mounted() {
    this.checkAuthenticated();
  },
  methods: {
    checkAuthenticated() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/login");
      } else {
        this.authenticated = true;
      }
    }
  }
};
</script>