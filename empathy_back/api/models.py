from django.db import models
from django.contrib.postgres.fields import ArrayField 

class Student(models.Model):
    name = models.CharField(max_length = 50, default = "naam")
    ide = models.CharField(max_length = 50)
    done = models.BooleanField(default = False)
    science = models.IntegerField(default = 0)
    moral_science = models.IntegerField(default = 0)
    social_studies = models.IntegerField(default = 0)
    maths = models.IntegerField(default = 0)
    computer = models.IntegerField(default = 0)
    literature = models.IntegerField(default = 0)
    def __str__(self):
        return self.ide

class DisorderPoint(models.Model):
    belongs_to = models.ForeignKey(Student, on_delete = models.CASCADE)
    adhd = models.IntegerField(default=0)
    asd = models.IntegerField(default=0)
    depression = models.IntegerField(default=0)
    ptsd = models.IntegerField(default=0)
    dyslexia = models.IntegerField(default=0)

class Question(models.Model):
    belongs_to = models.ForeignKey(Student, on_delete = models.CASCADE)
    ide = models.BigIntegerField()
    question = models.CharField(max_length = 250)
    answer = models.CharField(max_length = 300)
    answer_creds = ArrayField(models.CharField(max_length = 10))
    datetime = models.DateTimeField(auto_now=True)

class ToAsk(models.Model):
    question = models.CharField(max_length = 500)
    answer_cred = ArrayField(models.CharField(max_length = 10))
    redirection = ArrayField(models.IntegerField(), 2)
    disorders_arr = ArrayField(models.CharField(max_length = 100))
    response_pos = models.CharField(max_length = 500)
    response_neg = models.CharField(max_length = 500)

    def __str__(self):
        return self.question + "\t" + str(self.redirection)

class Feeling(models.Model):
    belongs_to = models.ForeignKey(Student, on_delete = models.CASCADE) 
    feeling = models.CharField(max_length = 100)
    hashed = models.BigIntegerField() 

class Sentiment(models.Model):
    belongs_to = models.ForeignKey(Student, on_delete = models.CASCADE)
    sentiment = models.BooleanField()