from django.shortcuts import render, redirect
from main import models
from ..import forms


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
    question_list = models.Question.objects.filter(interview=pk).order_by('sort_id')
    questionanswerpairs = {}
    for question in question_list:
        match question.type:
            case "text":
                answerform = forms.answer_text()
            case "longtext":
                answerform = forms.answer_longtext()
            case "image":
                answerform = forms.answer_image()
            case "boolean":
                answerform = forms.answer_boolean()
            case _:
                return
        questionanswerpairs[question] = answerform
    print(questionanswerpairs)

    ctx = {
        "questionanswerpairs" : questionanswerpairs
        }
    return render(request, 'app_write/interview.html', ctx)

