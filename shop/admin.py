from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'desc',)  # указываем названия полей как в модели
    list_editable = ('desc',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product',)  # указываем названия полей как в модели
