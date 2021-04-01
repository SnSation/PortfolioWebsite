from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

def index(request):
    template_path = 'main/index.html'
    context = {

    }
    return render(request, template_path, context)

def projects(request):
    template_path = 'main/projects.html'
    context = {

    }
    return render(request, template_path, context)