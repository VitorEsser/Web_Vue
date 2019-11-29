<template>
  <section class="container">
    <h1 align="center">BEM VINDO AO </h1> 
    <h2 align="center">SOS - CLÍNICA DE VACINAÇÃO!!</h2>
    <div>
      <blockquote class="blockquote">SOS - Clinica de vacinação surgiu com o proposito de auxiliar você e seu pet, com visão do mundo baseada nas boas relações com os seres vivos.<br>
        Problemas comuns nas clinicas:<br> Dificuldade no atendimento e no relacionamento com o pet; Dificuldade na parceria de cliente para profissional.<br>
        Solução que a SOS encontrou:<br> Fazer atividades com seu pet para conhecer-lo melhor; sempre procurar uma forma de entendimento entre cliente e profissional, pra chegar em um acordo.</blockquote>
    </div>
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