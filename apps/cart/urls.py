from django.urls import path
from apps.cart.views import carrinho,remove_cart,add_cart,remove_item_global,checkout


urlpatterns=[
    path('carrinho/',carrinho,name='carrinho'),
    path('add_cart/<int:product_id>',add_cart,name='add_cart'),
    path('remove_cart/<int:product_id>',remove_cart,name='remove'),
    path('remove_item_global/<int:product_id>',remove_item_global,name='removeglobal'),

    path('checkout',checkout,name='checkout')
]