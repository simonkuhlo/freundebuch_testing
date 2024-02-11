from django.shortcuts import render, redirect

from main import models
from . import new_entry_helpers
from ..models import ConfirmLink
from main import models as mainmodels


def check_auth(request, lang, auth_str):

    try:
        model = ConfirmLink.objects.get(confirmation_string=auth_str)
    except Exception:
        return render(request, 'app_write/auth/error.html')

    
    entry = model.entry

    entry.visible = True
    entry.save()

    model.delete()