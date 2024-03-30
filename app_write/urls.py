from django.urls import path
from . import views 

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('new_entry/', views.new_entry.handle_author_creation, name = "edit.create_author"),
    path('new_entry/author=<str:author>', views.new_entry.handle_interview, name = "edit.new_entry.interview"),
    path('new_entry/auth/<str:auth_str>', views.authentication.handle_authorize_by_url, name = "edit.new_entry.auth"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)