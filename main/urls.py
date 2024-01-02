from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('view/', include('app_read.urls'), name = 'view'),
    path('edit/', include('app_write.urls'), name = 'edit'),
]