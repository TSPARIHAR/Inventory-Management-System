from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Vendor, Sale
from .serializers import ProductSerializer, VendorSerializer, SaleSerializer

def home(request):
    return render(request, 'home.html')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
