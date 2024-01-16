from django.contrib import admin
from django.urls import path
from krishi import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("krishi/", views.krishi_index, name='krishi_home'),
    path("about/", views.about, name="about"),   
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
