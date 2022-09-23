from django.urls import path
from .import views

urlpatterns = [
    path('loggin/', views.login, name='login'),
    path('register/', views.register, name='register'),
]