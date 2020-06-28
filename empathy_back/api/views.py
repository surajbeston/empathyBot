from django.shortcuts import render
import random
import string
from .models import Student, ToAsk, DisorderPoint, Question, Feeling, Sentiment
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

from .questions import questions, answer_creds, response_neg, response_pos, redirection, disorders_arr
@csrf_exempt
def test(request):
    ide = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)])
    student = Student(ide = ide)
    student.save()
    return render(request, "api/test.html", {"room_name":ide })

@csrf_exempt
def get_id(request):
    ide = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)])
    student = Student(ide = ide)
    student.save()
    return JsonResponse({"id": ide})

@csrf_exempt
def create_questions(request):
    print (len())
    for i, question in enumerate(questions):
        obj = ToAsk(question = question, answer_cred = answer_creds[i], redirection = redirection[i], \
            disorders_arr = disorders_arr[i], response_neg = response_neg[i], response_pos = response_pos[i])
        obj.save()    
    return HttpResponse("Done")

@csrf_exempt
def marks_db(request):
    data = pd.read_csv("5.csv")
    for i, datum in enumerate(data.values):
        if i > 0:
            obj = Student(name = datum[0], ide = datum[1], science = datum[2], moral_science = datum[3], computer = datum[4],\
                 maths = datum[5], literature = datum[6], social_studies = datum[7])
            obj.save()
    return HttpResponse("done")

@csrf_exempt
def analyse(request, ide):
    student = Student.objects.get(ide = ide)
    point_obj = DisorderPoint.objects.get(belongs_to = student)
    points = [point_obj.adhd, point_obj.asd, point_obj.depression, point_obj.dyslexia, point_obj.ptsd]
    all_disorders = ["Attention Deficit Hyperactivity Disorder", "Autism Spectrum Disorder", "Depression", "Dyslexia", "Post Traumatic Stress Diorder"]
    disorders = []
    for i, point in enumerate(points):
        if point >= 2:
            disorders.append(all_disorders[i])
    all_sentiment = Sentiment.objects.filter(belongs_to = student)
    sentiments = [obj.sentiment for obj in all_sentiment]
    binArr = []
    for sentiment in sentiments :
        if sentiment:
            binArr.append(1)
        else:
            binArr.append(0)
    
    _sum  = sum(binArr)
    if (_sum/len(sentiments)) > 0.5:
        sentiment = "POSITIVE"
    else:
        sentiment = "NEGATIVE"

    all_feelings = Feeling.objects.filter(belongs_to = student)
    feelings = [obj.feeling for obj in all_feelings]

    questions = Question.objects.filter(belongs_to = student)
    question_arr = [[question.question, question.answer]for question in questions] 
    return JsonResponse({"ide": ide,"name": student.name, "sentiment": sentiment, "question_arr": question_arr, "feelings": feelings, "disorders": disorders })





@csrf_exempt
def get_data(request):
    toasks = ToAsk.objects.all()
    questions = []
    answer_creds = []
    redirection = []
    disorders_arr = []
    response_pos = []
    response_neg = []
    for toask in toasks:
        questions.append(toask.question)
        answer_creds.append(toask.answer_cred)
        redirection.append(toask.redirection)
        disorders_arr.append(toask.disorders_arr)
        response_pos.append(toask.response_pos)
        response_neg.append(toask.response_neg)
    return JsonResponse([{"questions": questions, "answer_creds": answer_creds, "redirection": redirection, "disorders_arr": disorders_arr,\
        "response_pos": response_pos, "response_neg": response_neg}], safe = False)


@csrf_exempt
def get_students(request):
    all_students = Student.objects.filter(done = True)
    students = [[student.ide, student.name] for student in all_students]
    return JsonResponse({"students": students})
    