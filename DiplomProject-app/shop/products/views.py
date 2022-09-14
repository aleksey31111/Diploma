from django.shortcuts import render


def index(request):
    context = {
        'title': 'Shop device',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Shop device - Каталог',
    }
    return render(request, 'products/products.html', context)
