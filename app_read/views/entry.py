from django.shortcuts import render, redirect
from django.forms import modelform_factory
from main import models

def main(request, entryid):
    entry = models.Entry.objects.get(id = entryid)
    language = entry.language
    all_answers = models.Answer.objects.filter(entry = entryid)
    
    #normal questions and answers
    item_dict = {} 
    for answer in all_answers:
        
        question = models.Question.objects.get(id = answer.question.id)
        if question.special == True:
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
            
        item_dict[question.sort_id] = item_info

    item_dict = dict(sorted(item_dict.items()))
    print(item_dict)
    ctx = { "item_dict" : item_dict}
    
    return render(request, 'app_read/view_entry.html', ctx)