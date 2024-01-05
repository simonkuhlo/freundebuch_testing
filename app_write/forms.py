from django import forms
from main import models


class select_interview(forms.Form):
    field1 = forms.ModelChoiceField(queryset=models.Interview.objects.all(), empty_label=None)


class answer_text(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['answer_text']
        labels = {
            "answer_text": ""
        }

class answer_longtext(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['answer_longtext']
        labels = {
            "answer_longtext": ""
        }

class answer_image(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['answer_image']
        labels = {
            "answer_image": ""
        }


class answer_boolean(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['answer_boolean']
        labels = {
            "answer_boolean": ""
        }
