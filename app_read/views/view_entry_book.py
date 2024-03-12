from django.shortcuts import render, redirect
from main import models


def main(request, lang, entryid):
    get_entry_info(entryid)


def get_entry_info(entryid):
    #set variables
    questions_per_page = 4
    
    #get everything
    entry = models.Entry.objects.get(id = entryid)
    author = entry.author
    author_name = author.name
    language = entry.language
    profile_picture_question = models.Question.objects.get(name = "profile_picture")
    profile_picture = models.Answer.objects.get(entry = entry, question = profile_picture_question.id)
    normal_answers = models.Answer.objects.filter(entry = entry, type = "answer_text")
    about_me = "Hallo"
    
    #sort information
    content_blocks = []
    content_page_1 = {
        "name" : author_name,
        "profile_picture" : profile_picture,
        "about_me" : about_me
    }
    content_blocks.append(content_page_1)
    
    #put questions into content blocks
    while len(normal_answers) > 0:
        no_of_questions = 0
        content_block = {}
        while no_of_questions < questions_per_page and len(normal_answers) > 0:
            no_of_questions += 1
            answer = normal_answers[0]
            question = models.Question.objects.get(id = answer.question.id)
            content_block[question] = answer
            normal_answers.pop(0)
        content_blocks.append(content_block)
            
    #pack information
    packed_entryinfo = []
    while len(content_blocks) > 0:
        page_site = 0
        packed_pageinfo = []
        while page_site < 2 and len(content_blocks) > 0:
            page_site += 1
            packed_pageinfo.append(content_blocks[0])
            content_blocks.pop(0)
        packed_entryinfo.append(packed_pageinfo)

    print(packed_entryinfo)
