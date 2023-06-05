from django.contrib import admin

from .models import Math_Choice, Math_Question

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Math_Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text"]
    search_fields = ["question_text"]

admin.site.register(Math_Question, QuestionAdmin)