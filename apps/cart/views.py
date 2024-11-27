from django.shortcuts import render,redirect,get_object_or_404
from apps.cart.models import Cart,CartItem
from apps.loja.models import  Loja
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.





def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request,product_id):
    produto = Loja.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    try:
        add_item = CartItem.objects.get(produto=produto,cart=cart)
        add_item.quantity += 1
        add_item.save()
    except CartItem.DoesNotExist:
        add_item = CartItem.objects.create(
            produto = produto,
            quantity = 1,
            cart=cart
        )
        add_item.save()
    return redirect('carrinho')



def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    produto = get_object_or_404(Loja,id=product_id)
    cart_item=CartItem.objects.get(produto=produto,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('carrinho')

def remove_item_global(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    produto=get_object_or_404(Loja,id=product_id)
    cart_item=CartItem.objects.get(produto=produto,cart=cart)
    cart_item.delete()
    return redirect('carrinho')

def carrinho(request,quantity=0,total=0,cart_items=None):
    taxa = 0
    totalglobal = 0
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total += (cart_item.produto.preco * cart_item.quantity)
            quantity += cart_item.quantity
        taxa = (2*total)/100
        totalglobal=taxa+total
    except ObjectDoesNotExist:
        pass

    context ={
        'total': total,
        'quantity': quantity,
        'cart_items':cart_items,
        'taxa':taxa,
        'totalglobal':totalglobal,

    }

    return render(request,'carrinho/carrinho.html',context)


def checkout(request,taxa=0,cart_items=None,totglobal=0,quantity=0,total = 0):
    if not request.user.is_authenticated:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(active=True,cart=cart)
            for cart_item in cart_items:
                total += (cart_item.produto.preco * cart_item.quantity)
                quantity += cart_item.quantity
            taxa = total/3
            totglobal=taxa+total

        except ObjectDoesNotExist:
            pass

        contextt = {
            'total': total,
            'quantity': quantity,
            'cart_items': cart_items,
            'taxa': taxa,
            'totalglobal': totglobal,

        }

    return render(request,'carrinho/checkout.html',contextt)






