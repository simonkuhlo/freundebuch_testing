from django.shortcuts import render
from main import models



# Create your views here.
def select_interview(request):
    return render(request, 'app_write/select_interview.html')

def interview(request, pk):
    question_list = models.Question.objects.filter(interview=pk).order_by('sort_id')
    ctx = {
        "questions" : question_list
        }
    return render(request, 'app_write/interview.html', ctx)