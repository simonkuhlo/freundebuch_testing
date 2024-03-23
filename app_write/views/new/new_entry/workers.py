from main import models
from django.forms import mode

from . import modelforms



def get_interview_elements(lang):
    for question in models.Question.objects.all().order_by('sort_id'):
        answerform = modelforms.get_answerform(question)
        