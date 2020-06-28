<template>
  <div class='result-component-main'>
    <div class="result-wrapper1">
      <div class="result-wrapper1 result11">
        <img src="../assets/result/success1.png" alt="success-vector">
      </div>
      <div id="disResult" class="result-wrapper1 result12">
        
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
        console.log(data.data);
        document.getElementById("disResult").innerHTML += data.data.ide
        document.getElementById("disResult").innerHTML += '<br>'
        document.getElementById("disResult").innerHTML += '<br>'
        document.getElementById("disResult").innerHTML += `possible disorders: `
        document.getElementById("disResult").innerHTML += '<br>'
        document.getElementById("disResult").innerHTML += `${data.data.disorders}`
        
        document.getElementById("disResult").innerHTML += '<br>'
        document.getElementById("disResult").innerHTML += '<br>'
        document.getElementById("disResult").innerHTML += `questions: `
        document.getElementById("disResult").innerHTML += '<br>'
        // data.data.question_arr.forEach(element => {
        //   console.log(element);
        // });
        document.getElementById("disResult").innerHTML += `${data.data.question_arr}`
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