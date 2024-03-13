from django.urls import path
from shop.views import (
    catalog, orders, create_order,
    product_detail,
)

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('orders/', orders, name='orders'),
    path('create_order/<int:id>/', create_order, name='create_order'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]
