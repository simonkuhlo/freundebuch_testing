from django.shortcuts import render, redirect
from django.forms import modelform_factory
from main import models

def main(request, lang, entryid):
    entry = models.Entry.objects.get(id = entryid)
    author = entry.author
    language = entry.language
    all_answers = models.Answer.objects.filter(entry = entry)

    
    #normal questions and answers
    normal_answers = {} 
    profile_picture = None
    author_name = author.name

    for answer in all_answers:
        question = models.Question.objects.get(id = answer.question.id)
        if question.special == True:
            if question.name == "profile_picture":
                profile_picture = answer.answer_image
            continue

        if question.type not in ["answer_text", "answer_longtext"]:
            continue

        match language:
            case "de":
                question_value = question.value_de
            case "en":
                question_value = question.value_en
        answer_text = answer.answer_text    

        item_info = {
            "question" : question_value,
            "answer" : answer_text
        }
            
        normal_answers[question.sort_id] = item_info

    normal_answers = dict(sorted(normal_answers.items()))
    ctx = {
        "author_name" : author_name, 
        "profile_picture" : profile_picture,
        "normal_answers" : normal_answers
        }
    
    return render(request, 'app_read/view_entry.html', ctx)