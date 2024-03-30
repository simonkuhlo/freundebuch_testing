from ...models import ConfirmLink



def authorize(auth_str):
    try:
        db_object = ConfirmLink.objects.get(confirmation_string=auth_str)
    except Exception:
        return False
    make_entry_visible(db_object.entry)
    db_object.delete()

def make_entry_visible(entry):
    entry.visible = True
    entry.save()