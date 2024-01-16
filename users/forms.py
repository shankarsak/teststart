from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User 
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # For translation

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['farm_name', 'first_name', 'last_name', 'address1', 'address2', 'contact_number']
        contact_number = forms.CharField(max_length=10)  
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit():
            raise forms.ValidationError("Contact number must be numeric.")
        if User.objects.filter(contact_number=contact_number).exists():
            raise ValidationError(_('Contact number already exists.'))
        if len(contact_number) != 10:
            raise forms.ValidationError("Contact number must be 10 digits long.")
        return contact_number
    def save(self, commit=True):
        user = super().save(commit=False)
        user.profile_complete = True  
        if commit:
            user.save()
        return user

class ProfileFormBuyer(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address1', 'address2', 'contact_number']
        contact_number = forms.CharField(max_length=10)  
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit():
            raise forms.ValidationError("Contact number must be numeric.")
        if len(contact_number) != 10:
            raise forms.ValidationError("Contact number must be 10 digits long.")
        return contact_number
    def save(self, commit=True):
        user = super().save(commit=False)
        user.profile_complete = True  
        if commit:
            user.save()
        return user