from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.listviews.home, name = "home"),
    path('home', views.views.home, name = "home"),
    path('entry/<str:entryid>', views.entry.main, name = "entry_view")
]