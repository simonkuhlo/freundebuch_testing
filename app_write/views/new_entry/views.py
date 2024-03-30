from . import workers
from . import renderers as render
from django.shortcuts import redirect
from django.urls import reverse

# views: decide what to render
# workers: backend tasks, getting content and saving content
# renderes: only display web page


def handle_interview(request, lang, author):
    if request.method == "POST":
        success = workers.save_interview(request, lang, author)
        if success:
            view = render.success(request, lang)
        else:
            view = render.error(request, lang)
    else:
        view = render.interview(request, lang)
    return view


def handle_author_creation(request, lang):
    if request.method == "POST":
        redirect = workers.save_author(request)
        if redirect != False:
            return redirect
        else:
            view = render.error(request, lang)
    else:
        view = render.create_author(request, lang)
    return view