<template>
  <v-app id="adoteEame">
    <ToolBar @toggle-drawer="$refs.drawer.drawer = !$refs.drawer.drawer"></ToolBar>
    <SideMenu id="sidemenu-theme" ref="drawer"></SideMenu>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import SideMenu from "@/components/SideMenu"
import ToolBar from "@/components/ToolBar"

export default {
  name: "App",
  components: {
    SideMenu: SideMenu,
    ToolBar: ToolBar
  }
};
</script>

<style>

  #sidemenu-theme{
    height: 300px !important;
    border-bottom: 1px solid gray;
  }
</style>

