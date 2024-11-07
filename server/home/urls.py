# home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('add-raw-material/', views.add_raw_material, name='add_raw_material'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('raw-materials/', views.raw_material_list, name='raw_material_list'),
]
