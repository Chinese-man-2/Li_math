import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class Math_Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text


class Math_Choice(models.Model):
    question = models.ForeignKey(Math_Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text