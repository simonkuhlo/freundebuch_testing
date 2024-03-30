from . import workers
from django.shortcuts import render




#Unfinished
def success(request, lang):
    ctx = {
        "language" : lang,
    }
    return render(request, 'app_write/create_author.html', ctx)
