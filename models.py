from django.db import models
from django.contrib.auth.models import User
from quizapp.models import Quiz
from  Question.models import questions

class Answers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question = models.ForeignKey(questions,on_delete=models.CASCADE)
    selected_option = models.IntegerField(null=True)
    score = models.IntegerField(default=0)



