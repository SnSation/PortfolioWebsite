from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    newest_questions = Question.objects.order_by('-pub_date')[:5]  
    output = ', '.join([f"Text: {question.question_text} | ID:{question.id}" for question in newest_questions])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Details: Question %s" % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s:"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're vogint on question %s:" % question_id)