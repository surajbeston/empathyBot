<template>
  <div class='admin-main'>
    <Header v-bind:activePage="pageName"/>
    <AdminComponent />
  </div>
</template>

<script>

import Header from "../components/Header";
import AdminComponent from "../components/Admin-component";

export default {
  name:'Admin',
  components: {
    Header,
    AdminComponent
  },
  data() {
    return {
      pageName: "home"
    }
  }

}

</script>

<style scoped>



</style>