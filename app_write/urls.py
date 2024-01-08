from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.views.home, name = "home"),
    path('new_entry/', views.selects.select_language, name = "new_entry"),
    path('new_entry/<str:language>', views.selects.select_interview, name = "new_entry"),
    path('new_entry/interview/<str:language>+<str:interview>', views.new_entry.interview, name = "new_entry"),
]