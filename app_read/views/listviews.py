from django.shortcuts import render, redirect
from django.forms import modelform_factory
from main import models




def home(request, lang):
    all_entries = models.Entry.objects.filter(visible=True).order_by('created')
    ctx = {
        "all_entries" : all_entries
    }

    return render(request, 'app_read/home.html', ctx)
