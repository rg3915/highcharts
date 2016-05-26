from django.contrib import admin
from .models import Dollar, Euro, Customer, Category, Product, Sale, SaleDetail

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Dollar)
admin.site.register(Euro)
