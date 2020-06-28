<template>
  <div class='result-component-main'>
    <div class="result-wrapper1">
      <div class="result-wrapper1 result11">
        <img src="../assets/result/success1.png" alt="success-vector">
      </div>
      <div class="result-wrapper1 result12">
        
      </div>
    </div>
  </div>
</template>

<script>

import axios from "axios"

export default {
  name:'ResultComponent',
  data() {
    return {
      serverIp: "165.22.211.244",
    }
  },
  mounted() {
    this.id = this.$route.params.id
    console.log(this.id);
    axios('http://'+ this.serverIp + "/analyse/"+ this.id)
      .then(data => {
        console.log(data);
      })
  }

}

</script>

<style scoped>

.result-wrapper1 {
  display: grid;
  padding: 0 2vw;
  grid-template-columns: auto auto;
  color: rgb(175, 207, 199);
}

.result11 > img {
  width: 700px;
}

</style>