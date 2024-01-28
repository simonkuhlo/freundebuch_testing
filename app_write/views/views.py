from django.shortcuts import render

# Create your views here.
def home(request, lang):
    return render(request, 'app_write/home.html')