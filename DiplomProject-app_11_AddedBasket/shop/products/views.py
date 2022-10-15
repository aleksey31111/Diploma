from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from products.models import Product, ProductCategory, Basket
from users.forms import UserProfileForm
    # ProfitableProposition, ProfitablePropositionCategory,


def index(request, category_id=None):
    user = request.user
    if user.is_authenticated and request.method == "POST":
        form = UserProfileForm(
            data=request.POST,
            files=request.FILES,
            instance=user)

        baskets = Basket.objects.filter(user=user)
        total_quantity = sum(basket.quantity for basket in baskets)
        total_sum = sum(basket.sum for basket in baskets)
        context = {
            'title': 'Shop device',
            'categories': ProductCategory.objects.all(),
            'products': Product.objects.all(),
            'form': form,
            'baskets': Basket.objects.filter(user=user),
            'total_quantity': total_quantity,
            'total_sum': total_sum,
            # 'profitablepropositions': ProfitableProposition.objects.all(),
        }
        if form.is_valid():
            form.save()
            return redirect('profile')

        if request.method == 'GET':
            form = UserProfileForm(instance=user)

    else:
        context = {
            'title': 'Shop device',
            'categories': ProductCategory.objects.all(),
            'products': Product.objects.all(),
        }
    if category_id:
        index = Product.objects.filter(category_id=category_id)
    else:
        index = Product.objects.all()
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


# def profitable_proposition(request, profitable_proposition_category_id=None):
#     context = {
#         'title': 'Shop device - Выгодное предложение',
#         'profitable_proposition_categories': ProfitablePropositionCategory.objects.all(),
#
#
#     }
#     if profitable_proposition_category_id:
#         profitable_proposition = ProfitableProposition.objects.filter(category_id=profitable_proposition_category_id)
#
#     else:
#         profitable_proposition = ProfitableProposition.objects.all()
#
#     paginator = Paginator(profitable_proposition, 5)  # Show 3 contacts per page.
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context.update({'profitable_proposition': page_obj})
#     return render(request, 'products/profitable_propositions.html', context)

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


# def profitable_proposition_basket_add(request, profitable_proposition_id):
#     # current_page = request.META.get("HTTP_REFERER")
#     product = ProfitableProposition.objects.get(id=profitable_proposition_id)
#     baskets = Basket.objects.filter(user=request.user, product=product)
#     # baskets = Basket.objects.filter(user=request.user, product=product)
#     if not baskets.exists():
#         basket = Basket(user=request.user, product=product, quantity=1)
#         basket.save()
#         # Basket.objects.create(user=request.user, product=product, quantity=1)
#         # return redirect(current_page)
#         return redirect(request.META.get("HTTP_REFERER"))
#     else:
#         basket = baskets.first()
#         basket.quantity += 1
#         basket.save()
#         return redirect(request.META.get("HTTP_REFERER"))


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return redirect(request.META.get("HTTP_REFERER"))
