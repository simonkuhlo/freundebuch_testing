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

        if question.type not in ["answer_text"]:
            continue

        match language:
            case "de":
                question_value = question.value_de
            case "en":
                question_value = question.value_en
        answer_text = answer.answer_text

        item_info = {
            "question" : question_value,
            "answer_text" : answer_text
        }
            
        normal_answers[question.sort_id] = item_info
        
    print(normal_answers)
    normal_answers = dict(sorted(normal_answers.items()))
    all_answers = answers_per_page(normal_answers)
    first_page_answers = all_answers[0]
    print(all_answers)
    del all_answers[0]
    print(all_answers)
    answer_pages = all_answers
    ctx = {
        "author_name" : author_name, 
        "profile_picture" : profile_picture,
        "first_page_answers" : first_page_answers,
        "answer_pages" : answer_pages,
        }
    
    return render(request, 'app_read/view_entry_book.html', ctx)

def answers_per_page(answer_dict):
    print(answer_dict)
    counter = 0
    first_page_questions = 2
    other_page_questions = 4
    first_page = True
    
    page_answer_list = []
    answer_list = []
    
    for item in answer_dict.items():
        answer_list.append(item[1])
        counter = counter + 1
        
        if first_page:
            if counter >= first_page_questions:
                page_answer_list.append(answer_list)
                answer_list = []
                counter = 0
                first_page = False
        else:
            if counter >= other_page_questions:
                print(f"test:{page_answer_list}")   
                page_answer_list.append(answer_list)
                counter = 0
                answer_list = []
    page_answer_list.append(answer_list)
    print(page_answer_list)         
    return page_answer_list