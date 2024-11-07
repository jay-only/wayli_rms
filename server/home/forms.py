# home/forms.py

from django import forms
from .models import Supplier, RawMaterial

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_email', 'contact_phone', 'address']

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = ['name', 'category', 'quantity', 'unit', 'unit_price', 'supplier', 'storage_location', 'reorder_level', 'price']
