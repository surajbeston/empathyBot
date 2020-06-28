import json
from channels.generic.websocket import WebsocketConsumer
from .questions import generator, initiator, processor, add_dynamics
from .models import Student


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)

        print (data)
        student = Student.objects.get(ide = data["ide"])
        if data["init"] == True:
            initiate_arr = initiator(data["ide"])
            self.send(text_data=json.dumps({
                'about': "initiator",'questions': initiate_arr[0], 'answer_creds': initiate_arr[1], "question_no": 0
            }))
            next_question = None
        else:
            if student.done == False:
                response, next_question, feeling, hashed = processor(data["ide"], data["question"], data["answer"], data["answer_creds"], data["answer_type"], data["question_no"])
                self.send(text_data=json.dumps({
                    'about': "response",'response': add_dynamics(response, "answer", data["answer"], data["ide"], feeling, hashed)
                }))
            else:
                self.send(text_data=json.dumps({
                    'about': "info",'response': "we are already done with our questions... have a nice day"
                }))

        if student.done == False:
            if next_question != None:
                question_arr = generator(data["ide"], next_question)
            else:
                question_arr = generator(data["ide"])
                next_question = 1

            if question_arr[0] == False:
                self.send(text_data=json.dumps({
                    'about': "exit", 'response': "thanks for answering all those questions. have a nice day."
                }))
            else:
                print (question_arr)
                self.send(text_data=json.dumps({
                        'about': "question",'question': question_arr[1], 'answer_creds': question_arr[2], "question_no": next_question
                    })) 