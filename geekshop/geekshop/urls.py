"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
=======
from django.urls import path

>>>>>>> 90ae9ea75642a8fad139b0e4e04c3ac457a35197
from mainapp import views as mainapp

urlpatterns = [
    path('', mainapp.index, name='main'),
    path('contact/', mainapp.contact, name='contact'),
<<<<<<< HEAD
    path('products/', include('mainapp.urls', namespace='products')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('products/', mainapp.products, name='products'),

    path('products/home/', mainapp.products_home, name='products_home'),
    path('products/office/', mainapp.products_office, name='products_office'),
    path('products/modern/', mainapp.products_modern, name='products_modern'),
    path('products/classic/', mainapp.products_classic, name='products_classic'),

    path('admin/', admin.site.urls),
]
>>>>>>> 90ae9ea75642a8fad139b0e4e04c3ac457a35197
