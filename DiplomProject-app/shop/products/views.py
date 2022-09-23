from django.shortcuts import render
from products.models import Product, ProductCategory, ProfitableProposition, ProfitablePropositionCategory
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Shop device',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'Shop device - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 6)  # Show 3 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'products': page_obj})
    return render(request, 'products/products.html', context)


def profitable_proposition(request, profitable_proposition_category_id=None):
    context = {
        'title': 'Shop device - Выгодное предложение',
        'profitable_proposition_categories': ProfitablePropositionCategory.objects.all(),

    }
    if profitable_proposition_category_id:
        profitable_proposition = ProfitableProposition.objects.filter(category_id=profitable_proposition_category_id)

    else:
        profitable_proposition = ProfitableProposition.objects.all()

    paginator = Paginator(profitable_proposition, 5)  # Show 3 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'profitable_proposition': page_obj})
    return render(request, 'products/profitable_propositions.html', context)


# def accessories(request, category_id=7):
#     context = {
#         'title': 'Диски',
#         'accessories': Product.objects.filter(category_id=category_id)
#     }
#     return render(request, 'products/accessories.html', context)
#
#
# def discs(request):
#     return render(request, 'products/discs.html')
#
#
# def robots(request):
#     return render(request, 'products/robots.html')
