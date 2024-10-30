from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm  # Import the custom form
from django.contrib import messages

# Register a new user and redirect to login page after registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth_app/register.html', {'form': form})

# Login view with login logic using AuthenticationForm
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    
    return render(request, 'auth_app/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('homepage')

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('homepage')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'auth_app/profile.html', {'form': form})

