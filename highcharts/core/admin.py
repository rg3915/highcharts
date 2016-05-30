from django.contrib import admin
from .models import Dollar, Euro, Customer, Category, Product, Sale, SaleDetail


@admin.register(Dollar)
class DollarAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_dollar'
    list_display = ['date_dollar', 'value']


@admin.register(Euro)
class EuroAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_euro'
    list_display = ['date_euro', 'value']


admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
