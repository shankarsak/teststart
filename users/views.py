from django.shortcuts import render, redirect, HttpResponse
from users.models import  User
from .forms import RegistrationForm, LoginForm, ProfileForm, ProfileFormBuyer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout, login as auth_login
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = LoginForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)  
        if form.is_valid():
            form.save()  
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('home')  
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ProfileForm(instance=request.user)  
    return render(request, 'complete_profile.html', {'form': form})

@login_required
def complete_profile_buyer(request):
    if request.user.role == 'Buyer':
        if request.method == 'POST':
            form = ProfileFormBuyer(request.POST, instance=request.user)  
            if form.is_valid():
                form.save()  
                messages.success(request, 'Your profile has been updated successfully!')
                return redirect('home')  
            else:
                messages.error(request, 'Please correct the errors in the form.')
        else:
            form = ProfileFormBuyer(instance=request.user)  
    return render(request, 'complete_profile_buyer.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')  
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form}) 

def logout_view(request):
    logout(request)
    return redirect('home')  

@login_required
def profile_view(request):
    user = request.user
    context = {'user': user}  
    return render(request, 'profile.html', context)
