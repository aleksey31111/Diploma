from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from products.models import Product, ProductCategory, Basket
from users.forms import UserProfileForm


# ProfitableProposition, ProfitablePropositionCategory,


def index(request, category_id=None):
    search_query = request.GET.get("search")
    context = {
        'title': 'Shop device',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    if category_id:
        index = Product.objects.filter(category_id=category_id)
    else:
        if search_query:
            products = Product.objects.filter(Q(name__icontains=search_query) |
                                              Q(short_description__icontains=search_query))
        else:
            products = Product.objects.all()
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    search_query = request.GET.get("search", "")
    context = {
        'title': 'Shop device - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        if search_query:
            products = Product.objects.filter(
                Q(name__icontains=search_query) |
                Q(short_description__icontains=search_query))
        else:
            products = Product.objects.all()

    paginator = Paginator(products, 6)  # Show 3 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'products': page_obj})
    return render(request, 'products/products.html', context)


@login_required(login_url='/users/login/')
def basket_add(request, product_id):
    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        # basket = Basket(user=request.user, product=product, quantity=1)
        # basket.save()
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return redirect(current_page)


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return redirect(request.META.get("HTTP_REFERER"))


# def detail_product(request, product_id):
#     context = {
#         'title': 'Shop device - Деталбный просмотр',
#         # 'product': Product.objects.filter(id=product_id),
#         'products': Product.objects.objects.all(),
#     }
#     if product_id:
#         context.update({'products'}) Product.objects.get(id=product_id)
#     # else:
#     #     product = Product.objects.all()
#     return render(request, 'products/detail_product.html', context)

# def detail_product(request):
#     model = Product
#     content = {
#
#     }


def detail_product(request, product_id=None):
    context = {
        'title': 'Shop device - Каталог',
        'categories': ProductCategory.objects.all(),
        'product': Product.objects.all()
    }
    # if category_id:
    #     products = Product.objects.filter(category_id=category_id)
    #     if product_id:
    #         product = Product.objects.filter(product_id=product_id)
    #     else:
    #         product = Product.object.all()
    # else:
    #     products = Product.objects.all()
    if product_id:
        product = Product.objects.filter(product_id=product_id)
    else:
        product = Product.object.all()
    # context.update({'product': page_obj})
    return render(request, 'products/detail_product.html', context)
