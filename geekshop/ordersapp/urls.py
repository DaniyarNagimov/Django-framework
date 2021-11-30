from django.urls import path
from ordersapp import views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='list'),
    path('read/<pk>/', ordersapp.OrderRead.as_view(), name='read'),
    path('create/', ordersapp.OrderCreate.as_view(), name='create'),
    path('update/<pk>/', ordersapp.OrderUpdate.as_view(), name='update'),
    path('delete/<pk>/', ordersapp.OrderDelete.as_view(), name='delete'),
    path('cancel/forming/<pk>/', ordersapp.order_forming_complete, name='forming_cancel'),
]
