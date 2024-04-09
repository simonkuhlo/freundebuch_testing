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
    pages = workers.get_all_interview_elements(lang)
    ctx = {
        "pages" : pages,
        "language" : lang,
    }
    return render(request, 'app_write/new_entry/interview.html', ctx)