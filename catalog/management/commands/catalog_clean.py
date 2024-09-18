from django.core.management.base import BaseCommand
# from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()