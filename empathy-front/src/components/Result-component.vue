<template>
  <div class='result-component-main'>
    <div class="result-wrapper1">
      <div class="result-wrapper1 result11">
        <img src="../assets/result/success1.png" alt="success-vector">
      </div>
      <div id="disResult" class="result-wrapper1 result12">
        <h1>{{name}}</h1>
        <h2>Possible Disorders:</h2>
        <div v-bind:key='disorder' v-for="disorder in disorders">
          <h4>{{disorder}}</h4>
        </div>
        <br>
        <h2>Feelings</h2>
        <div v-bind:key='fee' v-for="fee in feelings">
          <h4>{{fee}}</h4>
        </div>
        <br>
        <h2>Sentiment:</h2>
        <h4>{{sentiment}}</h4>
        <br>
        <h2>Questions:</h2>
        <div v-bind:key="question" v-for='question in questions'>
          <br>
          <h4>{{question[0]}}</h4>
          
          <h5>answer: {{question[1]}}</h5>
        </div>
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
      sentiment: '',
      questions: [],
      disorders: [],
      name: '',
      feelings: [],
      serverIp: "165.22.211.244",
    }
  },
  mounted() {
    this.id = this.$route.params.id
    console.log(this.id);
    axios('http://'+ this.serverIp + "/analyse/"+ this.id)
      .then(data => {
        console.log(data.data);
        this.name = data.data.name
        this.questions = data.data.question_arr
        this.feelings = data.data.feelings
        this.disorders = data.data.disorders
        this.sentiment = data.data.sentiment
        // document.getElementById("disResult").innerHTML += data.data.ide
        // document.getElementById("disResult").innerHTML += '<br>'
        // document.getElementById("disResult").innerHTML += '<br>'
        // document.getElementById("disResult").innerHTML += `possible disorders: `
        // document.getElementById("disResult").innerHTML += '<br>'
        // document.getElementById("disResult").innerHTML += `${data.data.disorders}`
        
        // document.getElementById("disResult").innerHTML += '<br>'
        // document.getElementById("disResult").innerHTML += '<br>'
        // document.getElementById("disResult").innerHTML += `questions: `
        // document.getElementById("disResult").innerHTML += '<br>'
        // // data.data.question_arr.forEach(element => {
        // //   console.log(element);
        // // });
        // document.getElementById("disResult").innerHTML += `${data.data.question_arr}`
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

.result12 {
  display: flex;
  flex-direction: column;
  max-height: 60vh;
  overflow-y: scroll;
}

</style>