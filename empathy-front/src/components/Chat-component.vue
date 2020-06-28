<template>
  <div class="chat-component-main">
    <div class="chat-wrapper1">
      <div class="chat11">
        <div class="chat11-messageContainer">
          <!-- all message goes here  -->
        </div>
        <div class="chat11-bottom">
          <div class="chat11-bottom-buttons">
            <!-- all buttons goes here  -->
          </div>
          <div class="chat11-bottom-number none">
            <input type="number" v-model="messageNumber" id="messageNumber" autocomplete="off" />
            <button class="btn-sendMessageNumber"><i class="fas fa-paper-plane"></i></button>
          </div>
          <div class="chat11-bottom-text none">
            <input
              type="text"
              v-model="message"
              id="message"
              placeholder="type your message here!"
              autocomplete="off"
            />
            <button class="btn-sendMessage"><i class="fas fa-paper-plane"></i></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "ChatComponent",
  data() {
    return {
      serverIp: "165.22.211.244",
      message: "",
      messageNumber: 0,
      MessageStyles:
        "padding: 10px 20px 10px 20px;margin-top: 20px;max-width: 70%;color: white;border-radius: 20px;",
      buttonStyles:
        "color:white;background-color: rgb(0, 180, 120);padding: 10px 20px 10px 20px;margin: 0px 5px 5px 5px;border:none;outline:none;font-size:16px;border-radius: 10px;",
    };
  },
  methods: {
    analyzeMessage(data) {
      // console.log(data);

      switch (data.about) {
        case "question":
          this.addMessage("incoming", data.question);
          this.scrollDown();
          var btnIsPresent = false;
          var textIsPresent = false;
          var numberIsPresent = false;

          data.answer_creds.forEach((eachCreds) => {
            if (eachCreds === "Text input") {
              const textInput = document.getElementsByClassName("chat11-bottom-text")[0];
              textInput.setAttribute("class", "chat11-bottom-text");
              textIsPresent = true;
            } else if (eachCreds === "Number inp") {
              const numberInput = document.getElementsByClassName("chat11-bottom-number")[0];
              numberInput.setAttribute("class", "chat11-bottom-number");
              numberIsPresent = true;
            } else {
              this.buttonCreator(eachCreds);
              btnIsPresent = true;
            }
          });

          if (btnIsPresent) {
            const buttons = document.getElementsByClassName("chat11-bottom-eachButton");
            buttons.forEach((eachButton) => {
              eachButton.addEventListener("click", (e) => {
                this.sendToSocket(
                  e.target.value,
                  data.question,
                  data.answer_creds,
                  e.target.value,
                  data.question_no
                );
              });
            });
          }
          if (textIsPresent) {
            NaN;
          }
          if (numberIsPresent) {
            NaN;
          }

          break;

        case "response":
          if (data.response !== "") {
            this.addMessage("incoming", data.response);
          }
          break;

        default:
      }
    },

    sendToSocket(answer, question, answer_creds, answer_type, question_no) {
      this.clientSocket.send(
        JSON.stringify({
          init: false,
          question,
          ide: this.id,
          answer_creds,
          answer,
          answer_type,
          question_no,
        })
      );
      this.addMessage("outgoing", answer);
      this.scrollDown();
      this.resetAll();
    },

    numberInputCreator() {
      this.sendToSocket(
        this.messageNumber,
        this.allData.question,
        this.allData.answer_creds,
        "Number inp",
        this.allData.question_no
      );
    },

    buttonCreator(name) {
      var button = document.createElement("button");
      var buttonText = document.createTextNode(name);
      button.appendChild(buttonText);
      button.setAttribute("class", "chat11-bottom-eachButton");
      button.setAttribute("style", this.buttonStyles);
      button.setAttribute("value", name);

      const bottomContainer = document.getElementsByClassName("chat11-bottom-buttons")[0];
      bottomContainer.appendChild(button);
    },

    textInputCreator() {
      if (this.message !== "") {
        this.sendToSocket(
          this.message,
          this.allData.question,
          this.allData.answer_creds,
          "Text input",
          this.allData.question_no
        );
      }
    },

    resetAll() {
      const textInput = document.getElementsByClassName("chat11-bottom-text")[0];
      textInput.setAttribute("class", "chat11-bottom-text none");
      const numberInput = document.getElementsByClassName("chat11-bottom-number")[0];
      numberInput.setAttribute("class", "chat11-bottom-number none");
      document.getElementsByClassName("chat11-bottom-buttons")[0].innerHTML = "";
    },

    incomingWrapper(givenMessage) {
      return `<div style="${this.MessageStyles}align-self:flex-start;background-color:dodgerblue;">${givenMessage}</div>`;
    },

    outgoingWrapper(givenMessage) {
      return `<div style="${this.MessageStyles}align-self:flex-end;background-color:rgb(0, 180, 120);">${givenMessage}</div>`;
    },

    scrollDown() {
      const messageContainer = document.getElementsByClassName("chat11-messageContainer")[0];
      messageContainer.scrollTop = messageContainer.scrollHeight;
    },

    addMessage(type, givenMessage) {
      if (givenMessage !== "") {
        const messageContainer = document.getElementsByClassName("chat11-messageContainer")[0];
        switch (type) {
          case "incoming":
            messageContainer.innerHTML += this.incomingWrapper(givenMessage);
            this.scrollDown();
            break;
          case "outgoing":
            messageContainer.innerHTML += this.outgoingWrapper(givenMessage);
            this.scrollDown();
            this.message = ""; // sorry but i have to use it :)
            break;
          default:
        }
      }
    },
  },
  mounted() {
    const textInput = document.getElementById("message");
    textInput.addEventListener("keyup", (e) => {
      if (e.keyCode === 13) {
        this.textInputCreator();
      }
    });

    const numberInput = document.getElementById("messageNumber");
    numberInput.addEventListener("keyup", (e) => {
      if (e.keyCode === 13) {
        this.numberInputCreator();
      }
    });

    const btnSendMessage = document.getElementsByClassName("btn-sendMessage")[0];
    btnSendMessage.addEventListener("click", () => {
      this.textInputCreator();
    });

    const btnSendMessageNumber = document.getElementsByClassName("btn-sendMessageNumber")[0];
    btnSendMessageNumber.addEventListener("click", () => {
      this.numberInputCreator();
    });

    // axios("http://" + this.serverIp + "/id")
    //   .then((data) => {
    this.id = this.$route.params.id;
    console.log(this.id);
    this.clientSocket = new WebSocket("ws://" + this.serverIp + "/ws/chat/" + this.id + "/");

    this.clientSocket.onopen = () => {
      console.log("Socket Created!");
      this.clientSocket.send(
        JSON.stringify({
          init: true,
          ide: this.id,
        })
      );
    };

    this.clientSocket.onmessage = (messageData) => {
      this.allData = JSON.parse(messageData.data);
      this.analyzeMessage(this.allData);
    };

    this.clientSocket.onclose = () => {
      console.log("Socket closed!");
    };
    // })
    // .catch(() => {
    //   console.log("error");
    // });
  },
};
</script>

<style scoped>
button {
  border: none;
  outline: none;
}

.chat-wrapper1 {
  display: grid;
  grid-template-columns: auto;
  justify-content: center;
  margin-top: 2vh;
}

.chat11 {
  height: 80vh;
  width: 50vw;
  min-width: 500px;
  background-color: rgba(255, 255, 255, 0.781);
  position: relative;
}

.chat11-messageContainer {
  display: flex;
  flex-direction: column;
  padding: 10px 10px 0px 10px;
  height: 83%;
  overflow-y: scroll;
}

.chat11-eachMessage {
  padding: 10px 20px 10px 20px;
  margin-top: 20px;
  max-width: 70%;
  color: white;
  border-radius: 20px;
}

.incoming-message {
  background-color: dodgerblue;
  align-self: flex-start;
}

.outgoing-message {
  background-color: rgb(0, 180, 120);
  align-self: flex-end;
}

.chat11-bottom {
  width: 100%;
  position: absolute;
  bottom: 0;
}

.chat11-bottom-buttons {
  max-width: 100%;
  display: flex;
}

.chat11-bottom-eachButton {
  color: white;
  background-color: dodgerblue;
  padding: 10px 20px 10px 20px;
  margin: 0px 5px 5px 5px;
}

.chat11-bottom-number > input {
  margin-left: 20%;
  font-size: 20px;
  width: 50%;
  padding: 6px 50px 6px 20px;
  outline: none;
  border: none;
  background: white;
  letter-spacing: 1.5px;
  border-radius: 20px;
  margin-bottom: 10px;
}

.chat11-bottom-number > button {
  width: 10%;
  font-size: 20px;
  padding: 6px;
  background-color: rgb(0, 180, 120);
  color: white;
  border-radius: 20px;
  margin-bottom: 10px;
}

.chat11-bottom-text > input {
  font-size: 20px;
  width: 90%;
  padding: 6px 50px 6px 20px;
  outline: none;
  border: none;
  background: white;
  letter-spacing: 1.5px;
}

.chat11-bottom-text > input:focus + button,
.chat11-bottom-text > input:focus {
  height: 7vh;
}

.chat11-bottom-text > button {
  width: 10%;
  font-size: 20px;
  padding: 6px;
  background-color: rgb(255, 255, 255);
  color: rgb(0, 180, 120);
}

.chat11-bottom > button:hover {
  cursor: pointer;
}

/* others */

.none {
  display: none;
}

::-webkit-scrollbar {
  width: 0px;
}
</style>
