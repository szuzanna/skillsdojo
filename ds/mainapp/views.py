from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def index(request):
    learn_options = ['IT', "Maths", "Physics"]
    context = {
        'learn_options': learn_options
    }
    return render(request, 'mainapp/index.html', context)

def questionnaire(request):
    context = {}
    return render(request, 'mainapp/questionnaire.html', context)