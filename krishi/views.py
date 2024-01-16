from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from product.models import Product
from .forms import ProductEditForm

@login_required
def krishi_index(request):
    if request.user.role == 'Krishi':
        products = Product.objects.filter(seller=request.user)  
        context = {'products': products}
        return render(request, 'krishi_index.html',context) 
    else:
        # Unauthorized access
        return HttpResponse("Unauthorized access")

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if product.seller != request.user:
        return redirect('krishi_home')  
    try:
        product.image.delete()
    except Exception as e:
        print(f"Error deleting image: {e}")
    product.delete()
    return redirect('krishi_home')

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if product.seller != request.user:  
        return redirect('krishi_home')

    form = ProductEditForm(instance=product)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('krishi_home')

    context = {'form': form}
    return render(request, 'edit_product.html', context)


def about(request):
    return HttpResponse("This is about page!!")