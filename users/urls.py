from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),    
    path("accounts/login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.complete_profile, name='complete_profile'),
    path('edit_profile_buyer/', views.complete_profile_buyer, name='complete_profile_buyer'), 
]
