from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from products.models import Product, ProductCategory, Basket
# from django.views import generic
from django.http import HttpResponse
from django.template import loader


# def detail(request, pk):
#     return HttpResponse("Детальная Информация о странице:", pk)

def detail_view(request):
    context = {
        'title': 'Detail',
        'names': Product.objects.filer(name='Наушники складные светодиодные'),
        'images': Product.image,
        'description': Product.description,
        'short_description': Product.short_description,
        'price': Product.price,
        'quantity': Product.quantity,
        'time': Product.time,
        'time_update': Product.time_update,
        'category': Product.category
    }
    return render(request, 'products/detail_view.html', context)


# def detail_view(request, pk=None):
#     # products = Product.objects.all()
#     # template = loader.get_template('products/detail_view.html')
#     # template_name = 'products/detail_view.html'
#     context = {
#         'title': 'Device',
#         'detail_view': Product.objects.all(),
#
#     }
#     if pk:
#         index = Product.objects.filter(pk=pk)
#     else:
#         index = Product.objects.all()
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'products/detail_view.html', context)

def index(request, category_id=None):
    context = {
        'title': 'Shop device',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
        # 'profitablepropositions': ProfitableProposition.objects.all(),
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

# class ProductsListView(generic.ListView):
#     model = Product
#     context_object_name = 'products_list'
#     template_name = 'products/products_list.html'

# class DetailView(generic.DetailView):
#     queryset = Product.objects.all()
#     context_object_name = 'detail_view'
#     template_name = 'products/detail_view.html'
#     def get_object(self):
#         obj = super().get_object()
#         obj.name
#         return obj
#     def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Товар'
    #     context['products_id'] = Product.objects.all()
    #     return context



#     try:
#         product_id = Product.objects.get(pk=pk)
#     except:
#         raise ("Такого товара Нет")
#     return render(request, 'products/detail_view.html',
#                   context={'product': product_id})


