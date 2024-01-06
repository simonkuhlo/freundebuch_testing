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
    for question in models.Question.objects.filter(interview=pk).order_by('sort_id'):
        fields = helpers.get_fields_for_question_type(question.type)
        form_class = modelform_factory(models.Answer, fields=fields)
        form = form_class(
            request.POST or None,
            files=request.FILES or None,
            prefix=f"question-{question.id}"
        )
        form.instance.question = question
        questionformpairs[question] = form

        if request.method == "POST":
            print(request.POST)
            if all([form.is_valid() for form in questionformpairs.values()]):
                entry = models.Entry.objects.get(id="3")
                form.instance.entry = entry
                form.save()
    ctx = {
            "interview_id" : pk,
            "questionformpairs" : questionformpairs
            }
    return render(request, 'app_write/interview.html', ctx)
