<template>
  <div>
    <section class="container">
      <h1 id="h1-home" align="center">BEM VINDO AO </h1> 
      <h2 align="center">SOS - CLÍNICA DE VACINAÇÃO!!</h2>
      <div id ="div-home" align="center">
        <blockquote class="blockquote">
          <p><strong>SOS - Clínica de vacinação</strong> surgiu com o proposito de auxiliar você e seu pet, com visão do mundo baseada nas boas relações com os seres vivos.
            Nós prezamos pela saúde do seu pet e tendo isso em mente contamos com vacinas que auxiliam no combate contra doenças e bactérias.
          </p>
          <p>
            A vacinação de cães e gatos é o método de proteção mais importante e eficiente contra as doenças infecciosas, já que proporciona imunidade sobre a doença e criação de anticorpos. Assim, caso o animal algum dia entre em contato com a doença, estará capacitado a bloqueá-la.
            O filhote que for vacinado, por exemplo, tem uma grande chance de contrair alguma doença infecciosa e não atingir a idade adulta. Já os adultos podem adoecer em qualquer momento de sua vida, se não vacinados.
          </p>
          <p>
            <strong>Problemas comuns nas clínicas:</strong> Dificuldade no atendimento e no relacionamento com o pet; Dificuldade na parceria de cliente para profissional.
            <strong>Solução que a SOS encontrou:</strong> Fazer atividades com seu pet para conhecer-lo melhor; sempre procurar uma forma de entendimento entre cliente e profissional, pra chegar em um acordo.
          </p>  
          </blockquote>
      </div>
    </section>
    <div id="div-theme"></div>
  </div>
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

<style>

  #h1-home{
    margin-top: 20px;
  }

  #div-home{
    border: 1px solid black;
    margin-top: 20px;
    height: 400px;
    text-align:justify;
    padding: 40px 20px;
  }

  #div-theme{
    background-image: url("http://portalmariliense.com/portal/wp-content/uploads/2018/12/Dezembro-Verde-Entrevias.jpg");
    background-size: 100% 100%;
    height: 300px;
    width: 1000px;
    margin-top: 50px;
    margin-left: auto;
    margin-right: auto;

  }
</style>>