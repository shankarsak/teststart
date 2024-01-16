from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'quality', 'amount', 'seller', 'seller_name', 'seller_contact', 'seller_address')  # Fields to show in list view
    list_filter = ('seller_name',) 
    search_fields = ('name',)  
    fields = ('name', 'price', 'image', 'quality', 'amount', 'seller', 'seller_name', 'seller_contact', 'seller_address')
    readonly_fields = ('seller',)

admin.site.register(Product, ProductAdmin)