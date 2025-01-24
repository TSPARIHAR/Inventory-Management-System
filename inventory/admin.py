from django.contrib import admin

# Register your models here.
from .models import Product, Vendor, Sale

admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Sale)
