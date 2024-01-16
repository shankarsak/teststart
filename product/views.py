from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.contrib import messages
from .models import Product  
from django.contrib.auth import get_user_model
from users.models import User

User = get_user_model()

def product_index(request):
    products = Product.objects.all()  
    context = {'products': products}
    return render(request, "product_index.html", context)

@login_required
def add_product(request):
    if request.user.role == 'Krishi':
        if not request.user.profile_complete:
            return redirect('complete_profile')
        elif request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)  
            if form.is_valid():
                product = form.save(commit=False)  
                product.seller = request.user
                product.seller_name = request.user.first_name + " " +  request.user.last_name   
                product.seller_contact = request.user.contact_number
                product.seller_address = request.user.address1 + " " + request.user.address2
                form.save()
                messages.success(request, "Your item has been added successfully!")
                return redirect('home')  
        else:
            form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def show_products(request):
    products = Product.objects.all()  
    context = {'products': products}
    return render(request, 'products.html', context)

@login_required
def show_product_details(request, product_id):
    products = Product.objects.get(id=product_id) 
    context =  {'products': products}
    return render(request, 'product_details.html', context)
