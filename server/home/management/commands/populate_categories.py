# home/management/commands/populate_categories.py

from django.core.management.base import BaseCommand
from home.models import IngredientCategory

class Command(BaseCommand):
    help = 'Populate IngredientCategory with default categories'

    def handle(self, *args, **kwargs):
        categories = ["Vegetables", "Meats", "Spices", "Dairy", "Beverages"]
        for category_name in categories:
            category, created = IngredientCategory.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added category "{category_name}"'))
            else:
                self.stdout.write(self.style.WARNING(f'Category "{category_name}" already exists'))
