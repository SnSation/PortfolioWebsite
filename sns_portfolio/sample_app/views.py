from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'sample_app/index.html'
    context_object_name = 'newest_questions'

    def get_queryset(self):
        """
        Return the 5 most recently published questions.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'sample_app/detail.html'

    def get_queryset(self):
        """
        Excludes questions in the database with a
        publish date in the future
        """

        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'sample_app/results.html'

# def index(request):
#     newest_questions = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'newest_questions':newest_questions,
#     }
#     return render(request, 'sample_app/index.html', context)

# def detail(request, question_id):
#     selected_question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'selected_question':selected_question,
#     }
#     return render(request, 'sample_app/detail.html', context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question':question,
#     }
#     return render(request, 'sample_app/results.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'sample_app/detail.html', {
            'question':question,
            'error_message':'No choice selected.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        redirect_url = reverse('sample_app:results', args=(question.id, ))
        return HttpResponseRedirect(redirect_url)