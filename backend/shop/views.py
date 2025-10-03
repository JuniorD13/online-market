
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, Order
from django.urls import reverse


def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products' : products})

def product_details(request, sluglink):
    product = get_object_or_404(Product, sluglink=sluglink)
    return render(request, 'shop/product_detail.html', {'product' : product})

def add_to_cart(request, sluglink):
    user = request.user
    product = get_object_or_404(Product, sluglink=sluglink)
    cart, _ = Cart.objects.get_or_create(user=user) # le underscore represente une variable qu'on utilise pas
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse('product_detail', kwargs={'sluglink': sluglink}))

def cart(request):
    panier = get_object_or_404(Cart, user=request.user)

    return render(request, 'shop/cart.html', {'orders' : panier.orders.all()})

def delete_cart(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect('home')