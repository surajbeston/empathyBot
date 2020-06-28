<template>
  <div class='header-main'>
    <div class="navbar">
      <div class="navbar-link-container">
        <router-link to="/" class="home">Home</router-link>
        <router-link to="/about" class="about">About</router-link>
        <router-link to="/help" class="help">Help</router-link>
      </div>
      <div class="navbar-logo">
        <span class="h-font">EMPATHY</span>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name:'Header',
  props: [
    "activePage"
  ],
  mounted() {
    const activeLink = document.getElementsByClassName(this.activePage)[0]
    activeLink.setAttribute('class', 'active-page')
  }

}

</script>

<style scoped>

.header-main {
  height: 100px;
}

.navbar-link-container {
  height: 100%;
  display: flex;
  padding-top: 20px;
  padding-left: 5vw;
  font-size: 20px;
}

.navbar-link-container > a {
  padding-right: 5vw;
  text-decoration: none;
  color: rgb(213, 255, 232); 
  transition: .5s;
}

.navbar-link-container > a:hover {
  font-weight: bold;
  font-size: 25px;
  transition: 1s;
}

.navbar-logo {
  position: absolute;
  top: 0;
  right: 5vw;
  font-size: 50px;
  color: rgb(151, 187, 179);
  letter-spacing: 5px;
}

/* dynamic */
.active-page {
  font-weight: bold;
  font-size: 25px;
}

</style>