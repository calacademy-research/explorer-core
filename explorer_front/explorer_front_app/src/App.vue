<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/images">Go to Collection Images</router-link>
      <router-link to="/map">Go to Collection Map</router-link>
      <router-link to="/islands">Go to Galapagos Isands Map</router-link>
      <router-link to="/threejs">ThreeJS</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

nav {
  display: flex;
  justify-content: space-around;
  background: #333;
  padding: 1em;
}

nav a {
  color: white;
  text-decoration: none;
  padding: 0.5em;
}

nav a.router-link-exact-active {
  background: #555;
  border-radius: 4px;
}
</style>
