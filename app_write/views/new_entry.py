from django.shortcuts import render, redirect

from main import models
from . import new_entry_helpers
from .. import forms


def interview(request, language, interview_id, author_id):
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
        
        entry = create_boilerplate(questionformpairs, language, interview_id)
        
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

def create_author(request, language):
    
    form = forms.create_author(request.POST or None)
    
    if request.method == 'POST':
        
        if form.is_valid():
            instance = form.save()
            # Get the 'next' parameter from the request
            next_url = request.get_full_path().replace("/create_author", "")
            print(next_url)
            return redirect(f'{next_url}/{instance.id}/3')
        
        else:

            return redirect(f'/edit/error')

    ctx = {
            "form" : form,
        }
    return render(request, 'app_write/create_author.html', ctx)



def create_boilerplate(bigdict, language, interview_id):
    #check for crucial questions and get their values
    for dict in bigdict.values():
        questioninfo = dict["info"]
        question_name = questioninfo["question_name"]
        #add other crucial questions here
        match question_name:
            case "name":
                author_name = dict["form"].cleaned_data['answer_text']
            case "fav_color":
                color = dict["form"].cleaned_data['answer_color']
            case "profile_picture":
                preview_image = dict["form"].cleaned_data['answer_image']
    
    # [!] Needs additions later. Check if author already exists, etc.
    author = models.Author.objects.create(name = author_name)
    interview = models.Interview.objects.get(id = interview_id)
    bg_color = new_entry_helpers.normalize_color(color)
    entry = models.Entry.objects.create(author = author, language = language, bg_color = bg_color, interview = interview, preview_image = preview_image)
    
    return entry
