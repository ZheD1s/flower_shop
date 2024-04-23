from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def homeView(request):
    return render(request,
                  'home.html',
                  context={
                      'flowers': Flower.objects.all(),
                      'bouquets':Bouquet.objects.all(),
                  })

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Flower.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Flower.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Flower.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Flower.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart.html')