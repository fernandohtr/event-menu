from django.contrib import admin

from v1.models import Product, Sponsor


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    ...
