from django.urls import path
from basketapp import views as basket

app_name = 'basketapp'

urlpatterns = [
    path('', basket.basket, name='basket'),
    path('add/<int:pk>/', basket.add, name='add'),
<<<<<<< HEAD
    path('remove/<int:pk>/', basket.remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basket.edit, name='edit'),
=======
    path('remove/<int:pk>/', basket.remove, name='remove')
>>>>>>> e972fac80de34039a4e3c2e81bf6c50c66cb1337
]