from django.shortcuts import render, redirect


from main import models
from . import helpers
from .. import forms


def interview(request, language, interview):
    questionformpairs = {}
    question_nr = 0
    for question in models.Question.objects.filter(interview=interview).order_by('sort_id'):
        form_class = helpers.get_form(question)
        form = form_class(
            request.POST or None,
            files=request.FILES or None,
            prefix=f"question-{question.id}"
        )
        
        form.instance.question = question
        
        question_info = helpers.get_question_info(language, question)
        questionformpairs[question_nr] = {"info" : question_info, "form" : form}
        
        question_nr += 1

    if request.method == "POST":
        for dict in questionformpairs.values():
            form = dict["form"]
            if form.is_valid():
                continue
            else:
                print("error")
                               
        author_name = questionformpairs[0]["form"].cleaned_data['answer_text']
        author = models.Author.objects.create(name = author_name)
        entry = models.Entry.objects.create(author = author)   
        for dict in questionformpairs.values():
            
            form.instance.entry = entry
            form.save()
        return redirect(f'/edit/new_entry/success')
            
    ctx = {
            "interview_id" : interview,
            "language" : language,
            "questionformpairs" : questionformpairs
            }
    return render(request, 'app_write/interview.html', ctx)
