from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('<str:lang>/', views.home, name = 'main.home'),
    path('<str:lang>/view/', include('app_read.urls'), name = 'view'),
    path('<str:lang>/edit/', include('app_write.urls'), name = 'edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)