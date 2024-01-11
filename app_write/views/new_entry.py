from django.shortcuts import render, redirect


from main import models
from . import new_entry_helpers
from .. import forms


def interview(request, language, interview_id):
    questionformpairs = {}
    question_nr = 0
    for question in models.Question.objects.filter(interview=interview_id).order_by('sort_id'):
        form_class = new_entry_helpers.get_form(question)
        form = form_class(
            request.POST or None,
            files=request.FILES or None,
            prefix=f"question-{question.id}"
        )
        
        form.instance.question = question

        question_info = new_entry_helpers.get_question_info(language, question)
        questionformpairs[question_nr] = {"info" : question_info, "form" : form}
        question_nr += 1

    if request.method == "POST":
        for dict in questionformpairs.values():
            form = dict["form"]
            if form.is_valid():
                continue
            else:
                # [!] Error page does not exist yet.
                render(request, 'app_write/new_entry/error')
        
        entry = create_boilerplate(questionformpairs, language)
        
        for dict in questionformpairs.values():
            form = dict["form"]
            form.instance.entry = entry
            form.save()
       
        # [!] Success page does not exist yet.
        return redirect(f'/edit/new_entry/success')
            
    ctx = {
            "interview_id" : interview_id,
            "language" : language,
            "questionformpairs" : questionformpairs
            }
    return render(request, 'app_write/interview.html', ctx)



def create_boilerplate(bigdict, language):
    #check for crucial questions and get their values
    for dict in bigdict.values():
        questioninfo = dict["info"]
        question_name = questioninfo["question_name"]
        #add other crucial questions here
        match question_name:
            case "name":
                author_name = dict["form"].cleaned_data['answer_text']
    
    # [!] Needs additions later. Check if author already exists, etc.
    author = models.Author.objects.create(name = author_name)
    entry = models.Entry.objects.create(author = author)
    entry.language = language
    return entry
