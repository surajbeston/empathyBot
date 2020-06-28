<template>
  <div class='chat-main'>
    <Header v-bind:activePage="pageName"/>
    <ChatComponent />
  </div>
</template>

<script>

import Header from "../components/Header";
import ChatComponent from "../components/Chat-component"

export default {
  name:'Chat',
  components: {
    Header,
    ChatComponent
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