from django.shortcuts import render, redirect
from django.forms import modelform_factory
from main import models
from . import helpers
from .. import forms


# Create your views here.
def select_interview(request):
    
    if request.method == 'POST':
        form = forms.select_interview(request.POST)
        if form.is_valid():
            selected_object = form.cleaned_data['field1']
            return redirect(f'/edit/new_entry/interview/{selected_object.id}')
        else:
            return redirect(f'/edit/error')
    form = forms.select_interview()
    ctx = {"form" : form,}
    return render(request, 'app_write/select_interview.html', ctx)

    

def interview(request, pk):
    questionformpairs = {}
    question_nr = 0
    for question in models.Question.objects.filter(interview=pk).order_by('sort_id'):
        fields = helpers.get_fields_for_question_type(question.type)
        form_class = modelform_factory(models.Answer, fields=fields)
        form = form_class(
            request.POST or None,
            files=request.FILES or None,
            prefix=f"question-{question.id}"
        )
        question_nr += 1
        form.instance.question = question
        questionformpairs[question] = form

    formlist = list(questionformpairs.values())

    if request.method == "POST":
        if all([form.is_valid() for form in questionformpairs.values()]):
            
            author_name = list(questionformpairs.values())[0].cleaned_data['answer_text']

            author = models.Author.objects.create(name = author_name)
            entry = models.Entry.objects.create(author = author)
            
            for form in questionformpairs.values():
                form.instance.entry = entry
                form.save()
    ctx = {
            "interview_id" : pk,
            "questionformpairs" : questionformpairs
            }
    return render(request, 'app_write/interview.html', ctx)
