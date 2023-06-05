from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from li_math.models import Math_Choice, Math_Question
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "li_math/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Math_Question.objects.filter().order_by("-id")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Math_Question
    template_name = "li_math/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Math_Question.objects.filter().order_by("-id")


class ResultsView(generic.DetailView):
    model = Math_Question
    template_name = "li_math/results.html"

def index(request):
    latest_question_list = Math_Question.objects()
    context = {"latest_question_list": latest_question_list}
    return render(request, "li_math/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Math_Question, pk=question_id)
    return render(request, "li_math/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Math_Question, pk=question_id)
    return render(request, "li_math/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Math_Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Math_Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "li_math/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("li_math:results", args=(question.id,)))

