from django.shortcuts import render, redirect

from main import models
from . import new_entry_helpers
from ..models import ConfirmLink
from main import models as mainmodels


def check_auth(request, auth_str):

    try:
        model = ConfirmLink.objects.get(confirmation_string=auth_str)
    except Exception:
        return render(request, 'app_write/auth/error.html')

    
    entry = mainmodels.Entry.objects.get(id = model.entry.id)
    print(entry)
    entry.visible = True
    entry.save()

    model.delete()