from django.shortcuts import render
from .models import Product,Carousel,Laptop,Accessories

from django.http import HttpResponse
def index(request):
    products=Product.objects.all()
    carousel=Carousel.objects.all()
    laptops=Laptop.objects.all()
    accessories=Accessories.objects.all()
    params={'products':products,'carousels':carousel,'laptops':laptops,'accessories':accessories}
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
    suggestions = Product.objects.all().exclude(id=id)
    url_parts='productview'
    params={'products':products,'product':product[0],'suggestions':suggestions,'url_parts':url_parts}
    return render(request,'shop/product.html',params)

def productViewLaptop(request, id):
    products=Laptop.objects.all()
    product = Laptop.objects.filter(id=id)
    suggestions = Laptop.objects.all().exclude(id=id)
    url_parts='productviewLaptop'
    params={'products':products,'product':product[0],'suggestions':suggestions,'url_parts':url_parts}
    return render(request,'shop/product.html',params)

def productViewAccessories(request, id):
    products=Accessories.objects.all()
    product = Accessories.objects.filter(id=id)
    suggestions = Accessories.objects.all().exclude(id=id)
    url_parts='productviewAccessories'
    params={'products':products,'product':product[0],'suggestions':suggestions,'url_parts':url_parts}
    return render(request,'shop/product.html',params)

def checkout(request):
    return HttpResponse("We are at checkout")
