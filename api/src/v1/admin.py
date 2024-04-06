from django.contrib import admin

from v1.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...
