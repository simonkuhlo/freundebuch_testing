from django.shortcuts import render, redirect

from main import models
from .. import forms

    

# Create your views here.


#select a Language
def select_language(request):
    
    form = forms.select_language(request.POST or None)
    
    if request.method == 'POST':
        
        if form.is_valid():
            language = form.cleaned_data['field']
            # [!] Needs improvement. '+3' stands for Interview with ID 3. Make more dynamic for future.
            return redirect(f'/edit/new_entry/{language}/create_author')
        else:
            return redirect(f'/edit/error')

    ctx = {
            "form" : form,
            #select_name gets displayed in Html template
            "select_name" : "Language"
        }
    return render(request, 'app_write/select.html', ctx)






#unused, currently only 1 interview for everyone
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

