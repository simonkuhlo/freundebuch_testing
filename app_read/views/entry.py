from django.shortcuts import render, redirect
from django.forms import modelform_factory
from main import models

def main(request, entryid):
    entry = models.Entry.objects.get(id = entryid)
    language = entry.language
    all_answers = models.Answer.objects.filter(entry = entryid)
    
    for answer in all_answers:
        question = models.Question.objects.get(id = answer.question.id)
        print(f"Question: {question}\nAnswer: {answer}")
    
    ctx = { "all_answers" : all_answers}
    
    return render(request, 'app_read/view_entry.html', ctx)