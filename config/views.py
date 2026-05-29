from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def cart_page(request):
    return render(request, "cart.html")

def login_page(request):
    return render(request, "login.html")

def checkout_page(request):
    return render(request, "checkout.html")

def product_detail(request, id):
    return render(request, "product_detail.html")