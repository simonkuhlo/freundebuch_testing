from django import forms
from main import models


class select_interview(forms.Form):
    field = forms.ModelChoiceField(queryset=models.Interview.objects.all(), empty_label=None)
    
    
class select_language(forms.Form):    
    field = forms.ChoiceField(choices=(("de","Deutsch"),("en","English")))
