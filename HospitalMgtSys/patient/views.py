from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, SignupForm
from .models import *

# from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def patient(request):
    patients = Patient.objects.all()
    return render(request, 'authentication/patient.html', {'patients' : patients})

def doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'authentication/doctor.html', {'doctors' : doctors})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
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

            if User.objects.filter(username=username).exists():
                error_message = 'Username already exists. Please choose a different username.'
                return render(request, 'authentication/signup.html', {'form': form, 'error_message': error_message})

            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'authentication/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
