from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Interview)
admin.site.register(models.Question)
admin.site.register(models.Entry)
admin.site.register(models.Answer)
admin.site.register(models.SystemMessage)
