from main import models
from . import forms

from django.shortcuts import redirect


def get_all_interview_elements(lang):
    for question in models.Question.objects.all().order_by('sort_id'):
        # get profile picture
        # get about me
        # get name
        
        # get all normal queations
        answerform = forms.get_answerform(question)
        print(f"Hallo{answerform}")

def save_author(request):
    form = forms.create_author(request.POST or None)
    if form.is_valid():
        instance = form.save()
        next_url = request.get_full_path().replace("/create_author/", "")
        return redirect(f'{next_url}author={instance.id}')
    else:
        return False
        