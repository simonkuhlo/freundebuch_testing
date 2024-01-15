from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('view/', include('app_read.urls'), name = 'view'),
    path('edit/', include('app_write.urls'), name = 'edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)