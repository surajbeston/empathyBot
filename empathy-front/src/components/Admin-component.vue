<template>
  <div class='admin-component-main'>
    <div class="admin1-wrapper">
      <h1>
        All Students
      </h1>
      <table>
        <tr>
          <th>Name</th>
          <th>Id</th>
          <th>Visit</th>
        </tr>
        <tr v-bind:key="student.id" v-for="student in allStudents">
          <td>{{student[1]}}</td>
          <td>{{student[0]}}</td>
          <td>
            <router-link :to="{name: 'Result', params: {id: student[0]}}">see result</router-link>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>

import axios from "axios"

export default {
  name:'AdminComponent',
  data() {
    return {
      allStudents: [],
      serverIp: "165.22.211.244"
    }
  },
  mounted() {
    axios('http://'+ this.serverIp + "/get_students")
      .then(data => {        
        this.allStudents = data.data.students
      })
    // this.allStudents = [['asdfasdfsadfasdfasfasdfasdfa', 'asdfasf']]
  }

}

</script>

<style scoped>

a {
  color: rgb(65, 233, 255);
  font-weight: bold;
  text-decoration: none;
}

.admin1-wrapper {
  display: grid;
  grid-template-columns: auto;
  justify-content: center;
}

.admin1-wrapper > h1 {
  width: 100%;
  font-size: 50px;
  letter-spacing: 2px;
  color: rgb(219, 255, 250);
}

.admin1-wrapper > table {
  text-align: center;
  width: 90vw;
  margin-top: 20px;
  color:rgb(197, 255, 250)
}

tr {
  margin-top: 50px;
}

th {
  /* border: 2px solid rgb(233, 254, 255); */
  font-size: 30px;
  background-color: rgba(0, 65, 65, 0.541);
}

td {
  font-size: 20px;
  letter-spacing: 1px;
}

</style>