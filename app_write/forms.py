from django import forms
from main import models


class select_interview(forms.Form):
    field1 = forms.ModelChoiceField(queryset=models.Interview.objects.all(), empty_label=None)