import random

from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> Lesson_6


def get_basket(user):
    if user.is_authenticated:
        return sum(list(Basket.objects.filter(user=user).values_list('quantity', flat=True)))
    return 0


def get_hot_product():
    return random.sample(list(Product.objects.all()), 1)[0]


def get_same_product(hot_product):
    return Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
<<<<<<< HEAD
=======
>>>>>>> e972fac80de34039a4e3c2e81bf6c50c66cb1337
=======
>>>>>>> Lesson_6


def index(request):
    context = {
        'title': 'Главная',
        'products': Product.objects.all()[:4],
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contact.html', context=context)


def products(request, pk=None):

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
<<<<<<< HEAD

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category_item = {
                'name': 'все'
            }
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'links_menu': links_menu,
            'title': title,
            'category': category_item,
            'products': products_list,
            'basket': get_basket(request.user)
        }

        return render(request, 'mainapp/products_list.html', context=context)

<<<<<<< HEAD
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)
=======
    hot_product = random.sample(list(Product.objects.all()), 1)[0]
    same_products = Product.objects.all()[3:5]
>>>>>>> e972fac80de34039a4e3c2e81bf6c50c66cb1337

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': get_basket(request.user)
    }

    return render(request, 'mainapp/products.html', context=context)


<<<<<<< HEAD
=======

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category_item = {
                'name': 'все'
            }
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'links_menu': links_menu,
            'title': title,
            'category': category_item,
            'products': products_list,
            'basket': get_basket(request.user)
        }

        return render(request, 'mainapp/products_list.html', context=context)

    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/products.html', context=context)


>>>>>>> Lesson_6
def product(request, pk):
    links_menu = ProductCategory.objects.all()
    context = {
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
        'links_menu': links_menu
    }
    return render(request, 'mainapp/product.html', context)
<<<<<<< HEAD
=======
def get_basket(user):
    if user.is_authenticated:
        return sum(list(Basket.objects.filter(user=user).values_list('quantity', flat=True)))
    return 0
>>>>>>> e972fac80de34039a4e3c2e81bf6c50c66cb1337
=======
>>>>>>> Lesson_6