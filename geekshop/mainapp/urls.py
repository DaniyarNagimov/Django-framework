from django.urls import path
from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('category/<int:pk>/', mainapp.products, name='category'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('product/<int:pk>/', mainapp.product, name='product')
=======
>>>>>>> e972fac80de34039a4e3c2e81bf6c50c66cb1337
=======
    path('product/<int:pk>/', mainapp.product, name='product')
>>>>>>> Lesson_6
]
