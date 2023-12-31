from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home', views.views.home, name = "home"),
    path('new_entry/', views.new_entry.select_interview, name = "select_interview"),
    path('new_entry/interview/<str:pk>', views.new_entry.interview, name = "new_entry"),
]