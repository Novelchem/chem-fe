<template>
  <div id="app" class="flex flex-col min-h-screen">
    <Navbar v-if="!$route.meta.hideNavbar" />
    <main class="flex-1 pt-20">
      <router-view></router-view> 
    </main>
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'; 
</script>

<style>
html {
  scroll-behavior: smooth;
}

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}
</style>