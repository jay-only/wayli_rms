# home/models.py

from django.db import models

class IngredientCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class RawMaterial(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('g', 'Grams'),
        ('L', 'Liters'),
        ('ml', 'Milliliters'),
        ('pcs', 'Pieces'),
        ('doz', 'dozen'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE, related_name='raw_materials')
    quantity = models.FloatField(help_text="Current quantity in stock")
    unit = models.CharField(max_length=5, choices=UNIT_CHOICES)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit",blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='raw_materials')
    storage_location = models.CharField(max_length=100, help_text="Location of the ingredient in storage")
    reorder_level = models.FloatField(help_text="Minimum quantity before reorder is needed")
    last_order_date = models.DateField(auto_now_add=True)
    last_restock_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    @property
    def total_value(self):
        return self.quantity * self.unit_price
