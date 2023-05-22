from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, SignupForm
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def patient(request):
    return render(request, 'authentication/patient.html')

def doctor(request):
    return render(request,'authentication/doctor.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired URL
            else:
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()
        error_message = ''

    return render(request, 'authentication/login.html', {'form': form, 'error_message': error_message})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(username=username, password=password)
            profile = UserProfile(user=user, first_name=first_name, last_name=last_name, email=email)
            profile.save()
            
            return redirect('login')  # Replace 'login' with your desired URL
    else:
        form = SignupForm()
        
    return render(request, 'authentication/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with your desired URL
