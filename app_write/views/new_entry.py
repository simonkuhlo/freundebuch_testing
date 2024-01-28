from django.shortcuts import render, redirect

from main import models
from . import new_entry_helpers
from .. import forms


def interview(request, lang, author, interview):
    questionformpairs = {}
    question_nr = 0
    for question in models.Question.objects.filter(interview=interview).order_by('sort_id'):
        form_class = new_entry_helpers.get_form(question)
        form = form_class(
            request.POST or None,
            files=request.FILES or None,
            prefix=f"question-{question.id}"
        )
        
        form.instance.question = question

        question_info = new_entry_helpers.get_question_info(lang, question)
        questionformpairs[question_nr] = {"info" : question_info, "form" : form}
        question_nr += 1

    if request.method == "POST":
        for dict in questionformpairs.values():
            form = dict["form"]
            if form.is_valid():
                continue
            else:
                # [!] Error page does not exist yet.
                render(request, 'app_write/new_entry/error')
        
        entry = new_entry_helpers.create_boilerplate(questionformpairs, lang, author, interview)
        
        for dict in questionformpairs.values():
            form = dict["form"]
            form.instance.entry = entry
            form.save()
       
        # [!] Success page does not exist yet.
        return redirect(f'/edit/new_entry/success')
            
    ctx = {
            "interview_id" : interview,
            "language" : lang,
            "questionformpairs" : questionformpairs
            }
    return render(request, 'app_write/interview.html', ctx)

def create_author(request, lang):
    
    form = forms.create_author(request.POST or None)
    
    if request.method == 'POST':
        
        if form.is_valid():
            instance = form.save()
            # Get the 'next' parameter from the request
            next_url = request.get_full_path().replace("/create_author", "")
            print(next_url)
            return redirect(f'{next_url}/author={instance.id}+interview=3')
        
        else:

            return redirect(f'/edit/error')

    ctx = {
            "form" : form,
        }
    return render(request, 'app_write/create_author.html', ctx)
