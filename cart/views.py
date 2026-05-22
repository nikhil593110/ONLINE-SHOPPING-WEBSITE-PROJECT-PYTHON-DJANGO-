from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart


def cart_details(request):
    cart = Cart(request)
    return render(request, 'cart/cart_details.html', {'cart': cart})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_details')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_details')

def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        cart.update(product=product, quantity=quantity)

    return redirect('cart_details')

