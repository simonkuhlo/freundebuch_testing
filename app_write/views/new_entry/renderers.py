from . import workers
from . import forms
from django.shortcuts import render, redirect


def create_author(request, lang):
    form = forms.create_author()
    ctx = {
        "form" : form,
        "language" : lang,
    }
    return render(request, 'app_write/create_author.html', ctx)



def interview(request, lang):
    interview_elements = workers.get_interview_elements(lang)
    ctx = {
        "interview_elements" : interview_elements,
        "language" : lang,
    }
    return render(request, 'app_write/interview.html', ctx)