from django.urls import path
# from . import views
from .views import login, register, profile, logout
    # ContactForm
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    # path('contact/', ContactFormView, name="contact"),
]
