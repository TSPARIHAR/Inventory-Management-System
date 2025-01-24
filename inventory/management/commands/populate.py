from django.core.management.base import BaseCommand
from inventory.models import Product, Vendor, Sale

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create sample vendors
        vendor1 = Vendor.objects.create(name='Vendor 1', contact='123-456-7890')
        vendor2 = Vendor.objects.create(name='Vendor 2', contact='987-654-3210')

        # Create sample products with price and stock quantity
        Product.objects.create(name='Product 1', sku='SKU001', category='Category 1', vendor=vendor1, price=10.99, stock_quantity=100)
        Product.objects.create(name='Product 2', sku='SKU002', category='Category 2', vendor=vendor2, price=15.49, stock_quantity=50)

        # Create sample sales
        Sale.objects.create(product=Product.objects.first(), quantity=10)
        Sale.objects.create(product=Product.objects.last(), quantity=5)

        self.stdout.write(self.style.SUCCESS('Sample data added successfully!'))
