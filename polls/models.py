import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
class Score(models.Model):
    score_text = models.CharField(max_length=20)
    def __str__(self):
        return self.score_text
    
class Score_Value(models.Model):
    question = models.ForeignKey(Score, on_delete=models.CASCADE, null=True)
    score_value_text = models.CharField(max_length=200)
    def __str__(self):
        return self.score_value_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.answer_text
    
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now