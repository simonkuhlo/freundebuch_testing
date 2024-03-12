from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.listviews.home, name = "view.home"),
    path('entry/<str:entryid>', views.view_entry_book.main, name = "view.view_entry")
]