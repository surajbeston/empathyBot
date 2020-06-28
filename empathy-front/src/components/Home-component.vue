<template>
  <div class="home-component-main">
    <div class="home-wrapper1">
      <div class="home-wrapper1 home11">
        <img src="../assets/home/success1.png" alt="success-vector">
      </div>
      <div class="home-wrapper1 home12">
        <h2>
          Empathy Bot is a chat bot that is designed to know a child through school academics record and through a set of questions, 
          with the help of which it can gain some insights about childs mental state. It can pre-diagonose some mental states or disorders 
          which can then help in complete diagnosis.
        </h2>
        <div class="home12-signinas">
          <h2>sign in as</h2>
          <router-link to="/admin">            
            <button class="btn-getstarted">administration  <i class="fas fa-chevron-right"></i></button>
          </router-link>
          <router-link :to="{name: 'Chat', params: {id: studentid}}">            
            <button class="btn-getstarted">student  <i class="fas fa-chevron-right"></i></button>
          </router-link>
          <!-- <button class="btn-getstarted">parent  <i class="fas fa-chevron-right"></i></button>  -->
          <input type="text" v-model="studentid" id="studentid" placeholder="enter student id if student">
        </div>
      </div>
    </div>
        <h1 style="color:white;">Use these ids for demo</h1>
        <div id="ids"></div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: "HomeComponent",
  data() {
    return {
      studentid: '',
      serverIp: "165.22.211.244",
    }
  },
  mounted() {
    axios('http://'+ this.serverIp + '/get_students_notdone')
      .then(data => {
        var students = data.data.students;
        students = students.slice(0, 5)
        var str = ''
        students.forEach(element => {
          str += element[0]
          str += '<br>' 
        });
        
        document.getElementById('ids').innerHTML = str
      })
  }
};
</script>

<style scoped>

#ids {
  color: white;
  letter-spacing: 2px;
}

.home-wrapper1 {
  display: grid;
  padding: 0 2vw;
  grid-template-columns: auto auto;
  color: rgb(175, 207, 199);
}

.home11 > img {
  width: 700px;
}

.home12 {
  /* position: relative; */
  display: grid;
  grid-template-columns: auto;
  margin-top: 15vh;
}


h2 {
  font-family: 'Open Sans', sans-serif;
}

.home12-signinas {
  margin-top: 5vh;
  margin-left: 5vw;
}

.home12-signinas > h2 {
  font-size: 40px;
  text-transform: uppercase;
  margin-bottom: 2vh;
}

.btn-getstarted {
  font-size: 20px;
  border-radius: 5px;
  background: none;
  border: 3px solid rgb(208, 245, 242);
  outline: none;
  height: 50px;
  width: 200px;
  color: rgb(153, 212, 197);
  margin: 10px;
}

.btn-getstarted:hover {
  color: white;
}

.home12-signinas > [type='text'] {
  font-size: 20px;
  font-weight: bold;
  background: none;
  border: none;
  border-bottom: 3px solid rgb(89, 143, 134);
  outline: none;
  text-align: center;
  width: 80%;
  margin-top: 50px;
  color: rgb(224, 255, 250);
  letter-spacing: 2px;
}

.home12-signinas > [type='text']:focus {
  transition: .5s;
  border-bottom: 3px solid rgb(255, 255, 255);
}

</style>
