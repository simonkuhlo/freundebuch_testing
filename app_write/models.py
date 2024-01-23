from django.db import models
from main import models as mainmodels



# Create your models here.
class ConfirmLink(models.Model):
    confirmation_string = models.CharField(max_length=100, unique = True)
    entry = models.ForeignKey(mainmodels.Entry, on_delete=models.CASCADE)