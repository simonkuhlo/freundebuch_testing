from . import workers
from django.shortcuts import render, redirect

#Structuring: Views should stay clean!!! Only get context variables, pass context and render. Rest should be done outside of views

def render_author_form(request, lang):
    pass

def render_interview(request, lang, author):
    interview_elements = workers.get_interview_elements(lang)
    ctx = {
        "interview_elements" : interview_elements,
        "language" : lang,
    }
    return render(request, 'app_write/interview.html', ctx)


def receive_interview(request, lang, author):
    if request.method == "POST":
        pass