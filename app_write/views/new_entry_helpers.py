from django import forms as djangoforms
from django.forms import modelform_factory
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
import string
import random
import numpy as np
from main import models
from .. import models as localmodels

class RequiredForm(djangoforms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequiredForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

def get_form(question):
    fields_and_widgets = get_fields_and_widgets_for_question_type(question.type)

    if question.required == True:
        form_class = modelform_factory(models.Answer, form=RequiredForm, fields=fields_and_widgets[0], widgets=fields_and_widgets[1])
    else:
        form_class = modelform_factory(models.Answer, fields=fields_and_widgets[0], widgets=fields_and_widgets[1])
    return form_class 

def get_fields_and_widgets_for_question_type(question_type):
    
    widgets = {}
    fields = [question_type]
    
    match question_type:
        case "answer_text":
            widgets = { 'answer_text' : djangoforms.TextInput(),}
        case "answer_longtext":  
            fields = ['answer_text']
            widgets = { 'answer_text' : djangoforms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        case "answer_boolean":
            widgets = { 'answer_boolean' : djangoforms.CheckboxInput(),}

        
    return [fields, widgets]



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

def create_boilerplate(bigdict, language, autohor_id, interview_id):
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
    author = models.Author.objects.get(id = autohor_id)
    interview = models.Interview.objects.get(id = interview_id)
    bg_color = normalize_color(color)
    entry = models.Entry.objects.create(author = author, language = language, bg_color = bg_color, interview = interview, preview_image = preview_image)
    send_confirmation_email(entry, author, language)
    return entry

def send_confirmation_email(entry, author, language):
    random_str = get_random_str(15)
    confirmation_link = reverse("edit.new_entry.auth", kwargs={"auth_str":random_str,"lang":language})
    localmodels.ConfirmLink.objects.create(confirmation_string = random_str, entry = entry)
    subject = "Simons Freundebuch - confirmation"
    message = confirmation_link
    from_mail = settings.EMAIL_HOST_USER
    to_mail = author.email
    match language:
        case "de":
            message = f"Hallo, {author.name}!\nUm deinen Eintrag Sichtbar zu machen bzw. ihn verwalten zu können, besuche folgende Adresse:\n{confirmation_link}"
        case "en":
            message = f"Hey, {author.name}!\nUm deinen Eintrag Sichtbar zu machen bzw. ihn verwalten zu können, besuche folgende Adresse:\n{confirmation_link}"
    send_mail(subject, message, from_mail, [to_mail], fail_silently=False,)


def get_random_str(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def normalize_color(color_str):
    color = color_str.replace("rgb(", "").replace(")", "")#format
    rgb_value = color.split(",")#format
    
    color_range = 100 #je niedriger, desto heller / farbloser
    rgb_center = (255, 255, 255) #mittelpunkt farbbereich
    
    x, y, z = np.array(rgb_value, dtype=int) - np.array(rgb_center)
    distance = np.sqrt(x**2 + y**2 + z**2)
    if distance <= color_range:
        return color_str
    else:
        x = round(rgb_center[0] + color_range * x / distance)
        y = round(rgb_center[1] + color_range * y / distance)
        z = round(rgb_center[2] + color_range * z / distance)
        new_rgb = f"rgb({x}, {y}, {z})"#format
        return new_rgb


