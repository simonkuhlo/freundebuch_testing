from django import forms as djangoforms
from django.forms import modelform_factory
from main import models


def get_form(question):
    fields_and_widgets = get_fields_and_widgets_for_question_type(question.type)
    form_class = modelform_factory(models.Answer, fields=fields_and_widgets[0], widgets=fields_and_widgets[1])
    return form_class  

def get_question_info(language, question):
    match language:
        case "de" : 
            question_text = question.value_de
            question_desc = question.description_de
        case "en" : 
            question_text = question.value_en
            question_desc = question.description_en
            
    info_dict = {
                "question_text" : question_text,
                "question_desc" : question_desc
    }    
    return info_dict

def get_fields_and_widgets_for_question_type(question_type):
    widgets = {}
    match question_type:
        case "text":
            fields = ['answer_text']
            widgets = { 'answer_text' : djangoforms.TextInput(),}
        case "longtext":  
            fields = ['answer_text']
            widgets = { 'answer_text' : djangoforms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        case "image":
            fields = ['answer_image']
        case "boolean":
            fields = ['answer_boolean']
        case _:
            return
    return [fields, widgets]