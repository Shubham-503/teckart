from django.shortcuts import render
from .models import Product,Carousel

from django.http import HttpResponse
def index(request):
    products=Product.objects.all()
    carousel=Carousel.objects.all()
    params={'products':products,'carousels':carousel}
    return render(request,'shop/index.html',params)

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request, id):
    products=Product.objects.all()
    product = Product.objects.filter(id=id)
    params={'products':products,'product':product[0]}
    return render(request,'shop/product.html',params)

def checkout(request):
    return HttpResponse("We are at checkout")
