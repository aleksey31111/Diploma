from django.urls import path
from .views import contact  # ContactCreate, success_page

urlpatterns = [
    # path('', ContactCreate.as_view(), name='contact'),
    # path('success/', success_page, name="success_page"),
    path('contact/', contact, name='contact'),
]
