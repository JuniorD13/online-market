from django.shortcuts import render, redirect
from .models import Product


def home(request):
    return render(request, 'shop/home.html', {'title' : home})
# Create your views here.
