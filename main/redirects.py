from django.shortcuts import redirect

def view(request):
    response = redirect('/view/home')
    return response