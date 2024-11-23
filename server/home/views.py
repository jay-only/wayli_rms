# home/views.py

from django.shortcuts import render, redirect
from .forms import SupplierForm, RawMaterialForm, ProductForm
from .models import Supplier, RawMaterial
from order.models import MenuItem


def home(request):
    return render(request, 'home/home.html')


def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'home/add_supplier.html', {'form': form})

def add_raw_material(request):
    if request.method == 'POST':
        form = RawMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('raw_material_list')
    else:
        form = RawMaterialForm()
    return render(request, 'home/add_raw_material.html', {'form': form})

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'home/supplier_list.html', {'suppliers': suppliers})

def raw_material_list(request):
    raw_materials = RawMaterial.objects.all()
    return render(request, 'home/raw_material_list.html', {'raw_materials': raw_materials})

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Add request.FILES
        if form.is_valid():
            form.save()
            print(request.FILES)
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'home/product.html', {'form': form})

def product_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'home/product_list.html', {'menu_items': menu_items})

