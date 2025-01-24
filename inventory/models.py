from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)  # Vendor name
    contact = models.CharField(max_length=50)  # Vendor contact details

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)  # Product name
    sku = models.CharField(max_length=50, unique=True)  # Unique product code
    category = models.CharField(max_length=50)  # Product category
    price = models.FloatField()  # Price per unit
    stock_quantity = models.IntegerField()  # Current stock quantity
    low_stock_threshold = models.IntegerField(default=10)  # Low stock warning threshold
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)  # Link to Vendor

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Sold product
    quantity = models.IntegerField()  # Quantity sold
    sale_date = models.DateTimeField(auto_now_add=True)  # Date of sale
