from django.shortcuts import render, redirect
from django.forms import modelform_factory
from main import models




def home(request):
    all_entries = models.Entry.objects.all().order_by('created')
    entry_list = []
    i = 0
    for entry in all_entries:
        if entry.visible == True:
            entry_list.append(entry)
    ctx = {
        "all_entries" : entry_list
    }

    return render(request, 'app_read/home.html', ctx)
