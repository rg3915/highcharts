from django.contrib import admin
from .models import Dollar, Euro, Category, Product


@admin.register(Dollar)
class DollarAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ['date', 'value']


@admin.register(Euro)
class EuroAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ['date', 'value']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'category']
    filter_list = ['category', ]


admin.site.register(Category)
