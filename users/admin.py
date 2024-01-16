from django.contrib import admin
from .models import User 
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'first_name', 'last_name', 'address1', 'address2', 'profile_complete', 'contact_number')  # Fields to show in list view
    list_filter = ('role',)  
    fields = ('username', 'email', 'role', 'first_name', 'last_name', 'address1', 'address2', 'contact_number')

admin.site.register(User, UserAdmin)  
