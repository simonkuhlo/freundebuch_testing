from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.views.home, name = "edit.home"),
    #start a new entry by selecting the language
    path('new_entry/', views.redirects.create_author, name = "edit.new_entry"),
    path('new_entry/create_author', views.new_entry.create_author, name = "edit.create_author"),
    #Interview form
    path('new_entry/author=<str:author>', views.new_entry.interview, name = "edit.new_entry.interview"),

    path('new_entry/auth/<str:auth_str>', views.auth.check_auth, name = "edit.new_entry.auth"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)