# home/views.py

from django.shortcuts import render, redirect
from .forms import SupplierForm, RawMaterialForm
from .models import Supplier, RawMaterial


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
