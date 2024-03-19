from main import models
from django.forms import mode




        
def get_interview_elements(lang):
    for question in models.Question.objects.all().order_by('sort_id'):
        pass