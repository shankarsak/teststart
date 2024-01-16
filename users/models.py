from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # For translation
        
class User(AbstractUser):
    ROLE_CHOICES = (
        ('Krishi', 'Krishi'),
        ('Buyer', 'Buyer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Krishi")
    profile_complete = models.BooleanField(default=False)
    # add it later
    farm_name = models.CharField(max_length=100, blank=True)
    address1 = models.CharField(max_length=255,blank=False)
    address2 = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True)
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(_('Email already exists.'))
        return email
