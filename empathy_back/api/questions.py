from .models import Question,  Student, DisorderPoint, ToAsk, Feeling, Sentiment
from datetime import datetime
import re
import random
import spacy
nlp = spacy.blank("en")
pipe = nlp.create_pipe("ner")
nlp.add_pipe(pipe)
data = open("model", "rb")
nlp.from_bytes(data.read())


import nltk
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

questions = ["--greet--, I\u2019m RoboEmpathy, your friend for a few minutes. I\u2019m a robot but quite --create-- to understand you. I\u2019ll be asking you some questions which you can choose to answer.  So, let us --start--\u2026", "So, --feeling--?", "How long have you been feeling this --bad--?", "Can you please explain your feelings?. Only little bit\u2026.", "Have you been feeling --tire-- and without energy for all these days?","Have you tried hurting yourself --recent--? I know it can be hard to share these things but you can try\u2026..", "Please click the third english alphabet from below...", "Please click the second english alphabet from below...", "Now, a sentence will be played and you\u2019ll have to write it below\u2026.", "Do you feel tired after reading, or do you feel reading tiresome?", "Do you regularly feel restless or are unable stay --idle--\u2026..", "So, do you have hard time concentrating even in dead-times, like during in --exam-- hall\u2026.", "Do you quickly forget about things you just had to remember?", "Well, we had a bit serious conversation, I really was wondering that does expressions of idioms and phrases like \u201cCuriosity killed the cat\u201d or \u201cDon\u2019t count your chickens before they hatch\u201d are confusing to you?", "Like a lot of people do you think handshakes and hugs and --weird-- and you try to avoid it\u2026.", "Do you get excessively passive or excessively aggressive or irritated in uncomfortable or unfamiliar situations?", "Do you find yourself in situations where you cannot define or imply facial expressions, sometimes verbal expressions like sarcasm, reasons to cry, etc.", "Are you always the first one to notice when a friend has gotten a haircut or made a small change to their appearance?", "Have you always wanted a best friend, but never found one?", "Do people say that you speak like a robot or abnormally?", "Have you experienced or witnessed a  major event, probably which had big negative impact on you? like someone\u2019s death...", "Having upsetting thoughts or images about the event that came into your head when you didn\u2019t want them to.", "Not feeling close to people around you?", "Being overly careful (for example, checking to see who is around you and what is around you)", "Feeling irritable or having fits of anger", "Do you often get nightmares, the scary ones that\u2019s related to something terrible that happened?", "I think you're quite smart. I just saw your marksheet and you've got quite low marks in  --subject--. Can you just tell your friend how you got these low marks"]

answer_creds = [["Yes", "Some other"], ["Good", "Bad", "Text input"], ["Number inp"], ["Text input"], ["Yes", "No"],["Yes", "No", "Text input"], ["c", "&#8580;"], ["b", "b"], ["Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Maybe", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"],  ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Yes", "No", "Text input"], ["Text input"]]

redirection = [[2, 0], [7, 3], [7, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 9], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 0], [17, 17], [18, 18], [19, 19], [20, 20],  [21, 21], [22, 22], [23, 23], [24, 24], [25, 25], [26, 26], [27, 27], [100, 100]]

disorders_arr = [[], [], ["0", "depression"], ["0", "depression"], ["depression", "0"],["depression", "0"], ["0", "dyslexia"], ["0", "dyslexia"], ["0", "dyslexia"], ["dyslexia", "0"], ["adhd", "0"], ["adhd", "0"], ["adhd", "0"], ["asd", "0"], ["asd", "0"], ["asd", "0"], ["asd", "0"], ["asd", "0"], ["asd", "0"],  ["asd", "0"], ["ptsd", "0"], ["ptsd", "0"], ["ptsd", "0"], ["ptsd", "0"], ["ptsd", "0"], ["ptsd", "0"], ["0", "Depression"]]

response_pos = ["", " I\u2019m happy that you\u2019re feeling --feel--", "Life has good and bad times.", "that\u2019s great", "", "Ok, you\u2019re doing good.", "That\u2019s great", "I\u2019m so sorry, it can so hard sometimes.", "Ok, you\u2019re doing good.", "You did well", "Happens to me too :D. Reading is very tedious task\u2026.", "A lot of people feel the same way ", "A lot of people feel the same way", "A lot of people feel the same way.", "Even I find it confusing", "Okay that\u2019s --interesting--. :D", "I\u2019m so sorry, it can be so hard sometimes.", "\\n", "Even I notice sometimes :D", "Oh, I\u2019m  really sorry to hear that --name--.",  "that\u2019s --cool-- --name--", "That\u2019s --trauma--", "I can understand. It is very hard.", "Oh,I am sorry to hear.", "Oh, I am sorry to hear.", "This issue is common.", "You are not alone(Person\u2019s name).", "Maybe you should just start working hard."]

response_neg = ["Its okay. We can chat some other time. Please don\u2019t forget to smile.", "I\u2019m so sorry that you\u2019re feeling --feel--", "I\u2019m so sorry you\u2019re feeling all these.", "", "I\u2019m so sorry, that I had to ask you this ", "That\u2019s great", "That\u2019s great", "There were little mistakes, but its okay ", "That\u2019s so smart of you", "Thats amaing", "I have to say, you\u2019re quite decent", "I have to say, you\u2019re quite decent", "I have to say, you\u2019re quite smart --name--.", "I have to say, you\u2019re quite smart.", "\\n", "\\n", "\\n", "\\n", "\\n", "\\n", "\\n", "Life has good and bad times.", "\\n", "\\n", "\\n", "\\n", "Things are tough sometimes."]

to_change = {"greet": ["hi", "hello", "namaste"], "create": ["designed", "made", "created"], "start": ["start", "begin"], \
    "feeling": ["how are you feeling", "are you feeling good"], "bad": ["bad", "not good"], "tire": ["tired", "tiresome"], \
        "recent": ["recently", "in the past",  ""], "idle": ["idle", "in one place"], "exam": ["exam", "test"], "trauma": ["bad", "traumatic"], "cool": ['very cool', 'cool', 'amazing', 'really cool'],\
            "interesting": ["very interesting", "interesting", "really interesting"], "weird": ["akward", "weird", "really weird"]
            }

good_words = ["happy", "good", "nice"]
bad_words = ["bad", "sad", "unhappy", "worse"]

def generator(ide, question_no = 1):
    print ("Questions number:  ",question_no)
    if question_no == 100:
        student = Student.objects.get(ide = ide)
        student.done = True
        student.save()
        return [False]
    toask = ToAsk.objects.get(id = question_no)
    return [True, add_dynamics( toask.question, "question", "0" ,ide), toask.answer_cred]

def add_dynamics(text, _for, answer, ide, feeling = None, hashed = None):
    if _for == "question":
        print (text)
        dynamic_elems = re.findall("--[a-zA-Z]+--", text)
        student_obj = Student.objects.get(ide = ide)
        for dynamic_elem in dynamic_elems:
            if dynamic_elem[2:-2] == "subject":
                marks = [student_obj.science, student_obj.social_studies, student_obj.maths, student_obj.literature, student_obj.moral_science, student_obj.computer]
                subjects = ["science", "social_studies", "maths", "literature", "moral_science", "computer"]
                subject = subjects[marks.index(min(marks))]
                text = text.replace(dynamic_elem, subject)
            elif dynamic_elem[2:-2] == "name":
                text = text.replace(dynamic_elem, student_obj.name)
            else:
                text = text.replace(dynamic_elem, random.choice(to_change[dynamic_elem[2:-2]]))
        print (text)
        return text
    elif _for == "answer":
        doc = nlp(answer)
        dynamic_elems = re.findall("--[a-zA-Z]+--", text)
        print (text)
        student_obj = Student.objects.get(ide = ide)
        for dynamic_elem in dynamic_elems:
            if dynamic_elem[2:-2] == "feel":
                if len(doc.ents) != 0:
                    for ent in doc.ents:
                        obj = Feeling(belongs_to = student_obj, feeling = str(ent), hashed = hashed)
                        obj.save()
                    word = str(random.choice(list(doc.ents)))
                    if feeling == "NEGATIVE" and word in good_words:
                        text = text.replace(dynamic_elem, "not "+ word)
                    elif feeling == "POSITIVE" and word in bad_words:
                        text = text.replace(dynamic_elem, "not " + word)
                    else:
                        text = text.replace(dynamic_elem, word)
                else:
                    if feeling == "POSITIVE":
                        text = text.replace(dynamic_elem, "good")
                    else:
                        text = text.replace(dynamic_elem, "bad")
            elif dynamic_elem[2:-2] == "name":
                text = text.replace(dynamic_elem, student_obj.name)
            else:
                text = text.replace(dynamic_elem, random.choice(to_change[dynamic_elem[2:-2]]))
        return text


def disorder_pointer(ide, disorder):
    obj = DisorderPoint.objects.get(belongs_to__ide = ide)
    if disorder == "depression":
        obj.depression += 1
    elif disorder == "adhd":
        obj.adhd +=1 
    elif disorder == "asd":
        obj.asd +=1
    elif disorder == "dyslexia":
        obj.dyslexia +=1
    elif disorder == "pstd":
        obj.disorder +=1
    obj.save()

def processor(ide, question, answer, answer_cred, answer_type, index):
    student = Student.objects.get(ide = ide)
    toask = ToAsk.objects.get(id = index)
    hashed =  hash(datetime.now())
    obj = Question(belongs_to = student, ide = hashed, question = question, answer_creds = answer_cred, answer = answer)
    obj.save()
    print ("Index:  ", index)
    feeling = ''
    print (feeling)
    if answer_type == "Text input":
        a = sid.polarity_scores(answer)
        print (a)
        if a["neg"] < a["pos"]:
            feeling = "POSITIVE"
            sent = Sentiment(belongs_to = student, sentiment = True)
            sent.save()
        else:
            feeling = "NEGATIVE"
            sent = Sentiment(belongs_to = student,sentiment = False)
            sent.save()
    elif answer_type == "Number input":
        if int(answer) < 10:
            feeling = "POSITIVE"
            sent = Sentiment(belongs_to = student, sentiment =True)
            sent.save()
        else:
            feeling = "NEGATIVE"
            sent = Sentiment(belongs_to = student, sentiment =False)
            sent.save()
    elif answer_type == "Good" or answer_type == "c" or answer_type == "b" or answer_type == "Yes":
        feeling = "POSITIVE"
    else:
        feeling = "NEGATIVE"
    
    if feeling== "POSITIVE":
        response = toask.response_pos
        next_question = toask.redirection[0]
        student 
        try:
            disorder_pointer(ide, toask.disorders_arr[0])
            print (toask.disorders_arr[0])
        except IndexError:
            pass 
    else:
        response = toask.response_neg
        next_question = toask.redirection[1]
        try:
            disorder_pointer(ide, toask.disorders_arr[1])
            print (toask.disorders_arr[1])
        except IndexError:
            pass 
    return response, next_question, feeling, hashed

def initiator(ide):
    all_questions = Question.objects.all()
    questions_ = []
    answers_ = []
    for question in all_questions:
        questions_.append(question.question)
        answers_.append(question.answer)    
    try:
        obj = DisorderPoint.objects.get(belongs_to__ide = ide)
    except: 
        student = Student.objects.get(ide=ide)
        obj = DisorderPoint(belongs_to  = student)
        obj.save()
    return [questions_, answers_]

