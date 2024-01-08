from django.shortcuts import render, redirect

from main import models
from .. import forms

    

# Create your views here.
def select_interview(request, language):
    if request.method == 'POST':
        form = forms.select_interview(request.POST)
        if form.is_valid():
            interview = form.cleaned_data['field']
            return redirect(f'/edit/new_entry/interview/{language}+{interview.id}')
        else:
            return redirect(f'/edit/error')
    form = forms.select_interview()
    ctx = {
            "form" : form,
            "select_name" : "Interview"
            }
    return render(request, 'app_write/select.html', ctx)


def select_language(request):
    if request.method == 'POST':
        form = forms.select_language(request.POST)
        if form.is_valid():
            language = form.cleaned_data['field']
            return redirect(f'/edit/new_entry/interview/{language}+3')
        else:
            return redirect(f'/edit/error')
    form = forms.select_language()
    ctx = {
            "form" : form,
            "select_name" : "Language"
        }
    return render(request, 'app_write/select.html', ctx)