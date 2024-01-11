from django.shortcuts import render, redirect
from django.forms import modelform_factory
from main import models




def home(request):
    all_entries = models.Entry.objects.all().order_by('created')
    entry_dict = {}
    i = 0
    for entry in all_entries:
        bg_color = models.Answer.objects.filter(question__name="bg_color", entry=entry.id).first().answer_text
        entry_dict[i] = {
            'entry' : entry,
            'bg_color' : bg_color
        }
        i += 1
    ctx = {
        "all_entries" : entry_dict
    }

    return render(request, 'app_read/home.html', ctx)
