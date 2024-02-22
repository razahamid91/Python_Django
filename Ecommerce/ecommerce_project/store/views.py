from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html',{'title': 'Home'})

def about(request):
    return render(request, 'about.html',{'title': 'About'})

def products(request):
    products_data =[
        {'name': 'products1', 'Price': 123.3},
        {'name': 'products2', 'Price': 12.3},
        {'name': 'products3', 'Price': 133.3},
        {'name': 'products4', 'Price': 113.3},

    ]
    return render(request, 'products.html',{'title': 'Products'})
