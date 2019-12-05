<template>
  <v-app-bar app :clipped-left="$vuetify.breakpoint.lgAndUp" color="#4EC796" dark>
    <v-app-bar-nav-icon
      @click.stop="$emit('toggle-drawer')"
    > </v-app-bar-nav-icon>    
    <v-toolbar-title>SOS - Clínica de Vacinação</v-toolbar-title>
  </v-app-bar>
</template>

<script>
import EventBus from "../main"
export default {
  name: 'ToolBar',
  props: ['drawer'],
  methods: {
    updateAppDrawer() {
      EventBus.$emit('updateAppDrawer')
    }
  }
}
</script>