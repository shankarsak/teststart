from django.db import models
from users.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/product_images')  
    quality = models.CharField(max_length=20, choices=(
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor'),
    ))
    amount = models.PositiveIntegerField()
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    seller_name = models.CharField(max_length=250, blank=True)
    seller_contact = models.IntegerField(blank=True, null=True)
    seller_address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name