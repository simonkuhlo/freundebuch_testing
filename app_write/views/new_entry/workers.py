from main import models
from . import forms

from django.shortcuts import redirect


def get_all_interview_elements(lang):

    #layout: [[{},{},{}],[{},{},...],...]
    all_pages = []

    # get name
    name = create_interview_element(mode="by_name", context="name")
    # get profile picture
    profile_picture = create_interview_element(mode="by_name", context="profile_picture")
    # get about me
    about_me = create_interview_element(mode="by_name", context="about_me")
    
    all_pages.append([name, profile_picture, about_me])
    
    # get all normal queations
    element_counter = 0
    current_page = []
    for question in models.Question.objects.filter(show_in_friendbook=True).order_by('sort_id'):
        interview_element = create_interview_element(mode="by_name", context=question.name)
        current_page.append(interview_element)
        element_counter += 1
        if element_counter >= 3:
            all_pages.append(current_page)
            current_page = []
            element_counter = 0
    if current_page != []:
        all_pages.append(current_page)
        
    #format for book view
    element_counter = 0
    formatted_page_list = []
    current_pages = []
    for page in all_pages:
        current_pages.append(page)
        element_counter += 1
        if element_counter == 2:
            formatted_page_list.append(current_pages)
            current_pages = []
            element_counter = 0
    if current_pages != []:
        formatted_page_list.append(current_pages)
        
    return formatted_page_list



def create_interview_element(mode:str, context):

    element_data = {
        "question" : None,
        "answer" : None,
    }

    if mode == "by_name":
        question = models.Question.objects.get(name=context)
        answerform = forms.get_answerform(question)
        element_data["question"] = question
        element_data["answer"] = answerform
    
    return element_data





def save_author(request):
    form = forms.create_author(request.POST or None)
    if form.is_valid():
        instance = form.save()
        next_url = request.get_full_path().replace("/create_author/", "")
        return redirect(f'{next_url}author={instance.id}')
    else:
        return False
        