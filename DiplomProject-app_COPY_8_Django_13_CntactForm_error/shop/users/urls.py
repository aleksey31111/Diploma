from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    # path('contact/', ContactFormView.as_view(), name="contact"),
    path(r'^contacts/$', views.EContactsView.as_view(), name='contacts'),
]
