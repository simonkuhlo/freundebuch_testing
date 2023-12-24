from django.shortcuts import redirect

def manager(request):
    response = redirect('/manager/home')
    return response