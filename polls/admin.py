from django.contrib import admin

from .models import Choice, Question, Answer, Score, Score_Value

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline, AnswerInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"] 
    search_fields = ["question_text"]

class Score_ValueInline(admin.TabularInline):
    model = Score_Value
    extra = 1

class ScoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["score_text"]})
    ]
    inlines = [Score_ValueInline]
    list_display = ["score_text"]
    list_filter = [] 
    search_fields = ["score_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Score,ScoreAdmin)