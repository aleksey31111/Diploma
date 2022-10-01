from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:category_id>', views.products, name='category'),
    path('products/<int:page>', views.products, name='page'),

    path('profitable_proposition/', views.profitable_proposition, name='profitable_proposition'),
    path('profitable_proposition/<int:profitable_proposition_category_id>',
         views.profitable_proposition, name='profitable_proposition_category'),
    path('profitable_proposition/<int:page>', views.profitable_proposition, name='page'),
    path('products/basket-add/<int:product_id>', views.basket_add, name="basket_add"),
    path(
        'profitable_proposition/basket-add/<int:profitable_proposition_id>',
        views.profitable_proposition_basket_add, name="profitable_proposition_basket_add"
    ),
    path('basket-add/<int:product_id>', views.basket_add, name="basket_add"),

    path('products/basket-delete/<int:id>', views.basket_delete, name="basket_delete")

]

