from django.contrib import admin
from .models import Restaurant, MenuItem, Category, Order, Payment

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Payment)

