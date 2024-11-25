from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Home or dashboard page
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    # path('tables/', views.tables, name='tables'),
    path('pos/', views.pos, name='pos'),
    # path('kitchen/', views.kitchen, name='kitchen'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),  # Log out
]
