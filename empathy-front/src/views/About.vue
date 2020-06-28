<template>
  <div class="about-main">
    <Header v-bind:activePage="pageName" />
    <span style="color:white;font-size:50px;">
      Not avilable, Sorry!
    </span>
  </div>
</template>

<script>
import Header from "../components/Header";

export default {
  name: "About",
  components: {
    Header,
  },
  data() {
    return {
      pageName: "about",
    };
  },
};
</script>

<style scoped>

.about-main {
  text-align: center;
}

</style>
