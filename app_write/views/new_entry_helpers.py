from django import forms as djangoforms
from django.forms import modelform_factory
import numpy as np
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
        "question_name" : question.name,
        "question_text" : question_text,
        "question_desc" : question_desc
    }    
    return info_dict

def get_fields_and_widgets_for_question_type(question_type):
    
    widgets = {}
    fields = [question_type]
    
    match question_type:
        case "answer_text":
            widgets = { 'answer_text' : djangoforms.TextInput(),}
        case "answer_longtext":  
            fields = ['answer_text']
            widgets = { 'answer_text' : djangoforms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        #case "answer_color":  
            #widgets = {'answer_color': djangoforms.TextInput(attrs={'type': 'color'}),}    
        #case "answer_image":
            
        case "answer_boolean":
            widgets = { 'answer_boolean' : djangoforms.CheckboxInput(),}
        #case _:
            #return
        
    return [fields, widgets]


def normalize_color(rgb_value):
    color_range = 100
    rgb_center = (255, 255, 255)
    
    x, y, z = np.array(rgb_value) - np.array(rgb_center)
    distance = np.sqrt(x**2 + y**2 + z**2)
    if distance <= color_range:
        return rgb_value
    else:
        x = round(rgb_center[0] + color_range * x / distance)
        y = round(rgb_center[1] + color_range * y / distance)
        z = round(rgb_center[2] + color_range * z / distance)
        new_rgb = (x, y, z)
        print(new_rgb)
        return new_rgb


