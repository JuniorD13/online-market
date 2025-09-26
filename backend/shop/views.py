from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products' : products})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product' : product})
# Create your views here.
