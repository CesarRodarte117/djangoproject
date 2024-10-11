# home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Ruta para la página principal
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]