from django.shortcuts import render


def home(request):
    return render(request, 'products/index.html')


def login(request):
    return render(request, 'products/login.html')


def signup(request):
    return render(request, 'products/signup.html')


def productDetailView(request):
    return render(request, 'products/viewdetails.html')
