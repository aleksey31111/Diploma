from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:category_id>', views.products, name='category'),
    path('products/<int:page>', views.products, name='page'),

    # path('accessories', views.accessories, name='accessories'),
    # path('discs/', views.discs, name='discs'),
    # path('robots/', views.robots, name='robots'),

    path('profitable_proposition/', views.profitable_proposition, name='profitable_proposition'),
    path('profitable_proposition/<int:profitable_proposition_category_id>',
         views.profitable_proposition, name='profitable_proposition_category'),
    path('profitable_proposition/<int:page>',
         views.profitable_proposition, name='page'),
    path('products/basket-add/<int:product_id>', views.basket_add, name="basket_add"),
    path('basket-add/<int:product_id>', views.basket_add, name="basket_add"),


]

