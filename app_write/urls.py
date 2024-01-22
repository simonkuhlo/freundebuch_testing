from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.views.home, name = "home"),
    #start a new entry by selecting the language
    path('new_entry/', views.selects.select_language, name = "create_author"),
    path('new_entry/<str:language>/create_author', views.new_entry.create_author, name = "new_entry"),
    #Interview form
    path('new_entry/<str:language>/author=<str:author>+interview=<str:interview>', views.new_entry.interview, name = "new_entry"),
    
    
    
    #select the interview to follow
    #path('new_entry/<str:language>', views.selects.select_interview, name = "new_entry"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)