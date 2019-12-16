from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'preview',)
    ordering = ('price', 'category',)
    list_filter = ('category',)
