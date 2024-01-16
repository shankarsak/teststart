from django.contrib import admin
from django.urls import path
from buyer import views

urlpatterns = [
    path("buyer/", views.buyer_index, name='buyer_home')    
]