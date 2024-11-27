from django.contrib import admin
from apps.cart.models import Cart,CartItem
# Register your models here.


class ListandoCart(admin.ModelAdmin):
    list_display = ('cart_id','date_add')

class ListandoCartItem(admin.ModelAdmin):
    list_display = ('produto','cart','quantity','active')


admin.site.register(Cart,ListandoCart)
admin.site.register(CartItem,ListandoCartItem)

