from django.shortcuts import render, redirect

def index(request):
    return redirect('login')

def login(request):
    """User login."""
    return render(request, 'registration/login.html')

def register(request):
    """User registration."""
    return render(request, 'registration/register.html')
