from django.db import transaction
from django.contrib import messages
from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
            with transaction.atomic():
                try:
                    super().save_model(request, obj, form, change)
                except Exception as e:
                    messages.set_level(request, messages.ERROR)
                    messages.error(request, e)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'preview',)
    ordering = ('price', 'category',)
    list_filter = ('category',)
