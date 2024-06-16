from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.

# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'ecommerce/product_list.html', context)

def home(request):
    return HttpResponse("<h1 style=color:purple;>Our web progress</h1>")