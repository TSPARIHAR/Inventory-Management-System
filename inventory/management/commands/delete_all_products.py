from django.core.management.base import BaseCommand
from inventory.models import Product

class Command(BaseCommand):
    help = 'Delete all products from the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All products have been deleted successfully!'))
