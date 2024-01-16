from django.contrib import admin
from django.urls import path
from product import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("product/", views.product_index, name='product_home'),
    #path("product_login/", views.product_index_login, name='product_home_login'),
    path('add_product/', views.add_product, name='add_product'),
    path('show_products/', views.show_products, name='show_product'),
    path('show_product_details/<int:product_id>/', views.show_product_details, name='show_product_details'),

] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
