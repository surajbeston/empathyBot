<template>
  <div class='result-main'>
    <Header v-bind:activePage="pageName"/>
    <ResultComponent />
  </div>
</template>

<script>

import Header from "../components/Header";
import ResultComponent from "../components/Result-component"

export default {
  name:'Result',
  components: {
    Header,
    ResultComponent
  },
  data() {
    return {
      pageName: 'home',
    }
  }

}

</script>

<style scoped>



</style>