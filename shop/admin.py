from django.contrib import admin

from .models import Product,Carousel,Laptop,Accessories
admin.site.register(Product)
admin.site.register(Carousel)
admin.site.register(Laptop)
admin.site.register(Accessories)