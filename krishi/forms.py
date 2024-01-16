from django import forms
from product.models import Product

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'quality', 'amount']
