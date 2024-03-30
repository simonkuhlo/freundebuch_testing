from . import workers
from . import renderers as render

# views: decide what to render
# workers: backend tasks, getting content and saving content
# renderes: only display web page


def handle_authorize_by_url(request, lang, auth_str):
    success = workers.authorize(auth_str)
    if success:
        view = render.success(request, lang)
    else:
        view = render.error(request, lang)
    return view