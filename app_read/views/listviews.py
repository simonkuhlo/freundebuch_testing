from django.shortcuts import render, redirect
from django.forms import modelform_factory
from main import models




def home(request):
    all_entries = models.Entry.objects.all().order_by('created')
    
    ctx = {
        "entries" : all_entries
    }
    
    return render(request, 'app_read/home.html', ctx)
