from django.shortcuts import redirect


def create_author(request, lang):
    url = request.get_full_path()
    return redirect(f'{url}create_author')
