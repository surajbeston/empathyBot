<template>
  <div class='chat-main'>
    <Header />
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
  }

}

</script>

<style scoped>



</style>