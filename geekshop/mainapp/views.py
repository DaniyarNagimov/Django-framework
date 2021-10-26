from django.shortcuts import render
<<<<<<< HEAD
from mainapp.models import Product, ProductCategory
=======
>>>>>>> 90ae9ea75642a8fad139b0e4e04c3ac457a35197


def index(request):
    context = {
<<<<<<< HEAD
        'title': 'Главная',
        'products': Product.objects.all()[:4]
=======
        'title': 'Главная'
>>>>>>> 90ae9ea75642a8fad139b0e4e04c3ac457a35197
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context=context)


<<<<<<< HEAD
def products(request, pk=None):
    context = {
        'links_menu': ProductCategory.objects.all(),
        'title': 'Подукты'
    }
    return render(request, 'mainapp/products.html', context=context)
=======
links_menu = [
    {
        'url': 'products',
        'title': 'все'
    },
    {
        'url': 'products_home',
        'title': 'Дом'
    },
    {
        'url': 'products_office',
        'title': 'Офис'
    },
    {
        'url': 'products_modern',
        'title': 'Модерн'
    },
    {
        'url': 'products_classic',
        'title': 'Класска'
    },

]


def products(request):
    context = {
        'links_menu': links_menu,
        'title': 'Подукты'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'Подукты для Дома'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'Подукты для Офиса'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'Подукты Модерн'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': 'Подукты Классика'
    }
    return render(request, 'mainapp/products.html', context=context)
>>>>>>> 90ae9ea75642a8fad139b0e4e04c3ac457a35197
