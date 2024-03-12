from django import forms
from main import models

    
    
class select_language(forms.Form):    
    field = forms.ChoiceField(choices=(("de","Deutsch"),("en","English")))


class create_author(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = "__all__"
