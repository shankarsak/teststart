from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name', 'price', 'image', 'quality', 'amount', 'seller',
            'seller_name', 'seller_contact', 'seller_address'
        )