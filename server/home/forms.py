# home/forms.py

from django import forms
from .models import Supplier, RawMaterial
from order.models import MenuItem

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_email', 'contact_phone', 'address']

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = ['name', 'category', 'quantity', 'unit', 'unit_price', 'supplier', 'storage_location', 'reorder_level', 'price']

class ProductForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'category', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }