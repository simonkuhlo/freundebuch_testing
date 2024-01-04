from django.shortcuts import render, redirect
from main import models
from ..import forms


# Create your views here.
def select_interview(request):
    
    if request.method == 'POST':
        form = forms.select_interview(request.POST)
        print(form)
        if form.is_valid():
            selected_object = form.cleaned_data['field1']
            return redirect(f'/edit/new_entry/interview/{selected_object.id}')
        else:
            return redirect(f'/edit/error')
    form = forms.select_interview()
    ctx = {"form" : form,}
    return render(request, 'app_write/select_interview.html', ctx)



def interview(request, pk):
    question_list = models.Question.objects.filter(interview=pk).order_by('sort_id')
    ctx = {
        "questions" : question_list
        }
    return render(request, 'app_write/interview.html', ctx)

