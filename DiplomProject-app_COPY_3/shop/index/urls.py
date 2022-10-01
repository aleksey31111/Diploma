from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/basket-add/<int:product_id>', views.basket_add, name="basket_add"),
]