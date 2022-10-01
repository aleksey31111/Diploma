from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from products.models import Product, ProductCategory, \
    ProfitableProposition, ProfitablePropositionCategory, Basket

def index(request, category_id=None):
    context = {
        'title': 'Shop device',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        index = Product.objects.filter(category_id=category_id)
    else:
        index = Product.objects.all()
    return render(request, 'products/index.html', context)


def basket_add(request, product_id):
    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        # basket = Basket(user=request.user, product=product, quantity=1)
        # basket.save()
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect(current_page)
