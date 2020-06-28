<template>
  <div class="home-main">
    <Header v-bind:activePage="pageName"/>
    <HomeComponent />
  </div>
</template>

<script>

import Header from "../components/Header"
import HomeComponent from "@/components/Home-component";

export default {
  name: 'Home',
  components: {
    Header,
    HomeComponent
  },
  data() {
    return {
      pageName: "home"
    }
  }
}
</script>
