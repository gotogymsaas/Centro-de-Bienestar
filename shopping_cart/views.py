from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product

def _get_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return cart

def add_to_cart(request, product_id):
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('shopping_cart:cart_detail')

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('shopping_cart:cart_detail')

def cart_detail(request):
    cart = _get_cart(request)
    return render(request, 'shopping_cart/cart_detail.html', {'cart': cart})
