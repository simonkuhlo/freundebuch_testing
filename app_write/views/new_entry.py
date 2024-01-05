from django.shortcuts import render, redirect
from main import models
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
    #get all questions
    question_list = models.Question.objects.filter(interview=pk).order_by('sort_id')

    #check if submission or not
    if request.method == 'POST':
        print(request.POST)

    else:
        questionanswerpairs = {}
        for question in question_list:
            
            #get question ID
            questionid = {"question" : str(question.id)}

            #get question type & create form
            match question.type:
                case "text":
                    answerform = forms.answer_text(initial=questionid)
                case "longtext":
                    answerform = forms.answer_longtext(initial=questionid)
                case "image":
                    answerform = forms.answer_image(initial=questionid)
                case "boolean":
                    answerform = forms.answer_boolean(initial=questionid)
                case _:
                    return
            
            #add question and form to dict
            questionanswerpairs[question] = answerform 

        #context
        ctx = {
            "interview_id" : pk,
            "questionanswerpairs" : questionanswerpairs
            }
        return render(request, 'app_write/interview.html', ctx)

