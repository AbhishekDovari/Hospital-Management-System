from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm, SignupForm, PatientForm, TreatmentForm
from .models import *
from .decorators import *
from django.views.generic import CreateView

# from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    patient = User.objects.filter(groups = 2)
    grp = request.user.groups.all()
    print(grp)
    return render(request, 'authentication/dashboard.html', {'patients': patient})

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient','doctor','admin'])
def patient(request):
    username = request.user.username
    patient = User.objects.filter(groups = 3 )
    return render(request, 'authentication/patient.html', {'patients' : patient , 'username': username})

@login_required
@allowed_users(allowed_roles=['doctor','patient'])
def patient_profile(request,pk):
    user = User.objects.filter(id = pk)
    pt = user[0]
    grp = request.user.groups.all()
    x=str(grp[0])
    print(grp)
    print(user[0])

    if(request.method == "POST"):
        form = TreatmentForm(request.POST)
        # if form.is_valid() :


    return render(request, 'authentication/patient_pro.html', {'user':pt, 'pk' : pk,'group':x })
    

@login_required(login_url='login')
def doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'authentication/doctor.html', {'doctors' : doctors})

@unauthenticated_user
def login_view(request):
    error_message = 'Invalid username or password.'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                grp = request.user.groups.all()
                print(grp[0])
                if(str(grp[0]) == "patient"):
                    print(grp[0])
                    return redirect('patient')
                else:
                    return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
                error_message = 'Invalid username or password.'
        else:
            messages.error(request, "Form is not valid.")
            error_message = 'Form is not valid.'

    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form, 'error_message': error_message})


def signup_view(request):
    if request.user.is_authenticated:
        if(request.user.groups.all() == 'patient'):
            return redirect('patient')
        else:
            return redirect('dashboard')
        
    else:
        error_message = 'Username already exists. Please choose a different username.'
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                

                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exists. Please choose a different username.')
                    error_message = 'Username already exists. Please choose a different username.'
                    return render(request, 'authentication/signup.html', {'form': form, 'error_message': error_message})

                user = User.objects.create_user(username=username, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.groups.set(form.cleaned_data['role'])
                user.save()
                
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
        else:
            form = SignupForm()

    return render(request, 'authentication/signup.html', {'form': form, 'error_message' : error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

def createPatient(request):
    
    form = PatientForm()
    
    return render(request, 'authentication/patientform.html', {'form':form})

def treatment(request):
    
    form = TreatmentForm()
    
    return render(request, 'authentication/treatment.html', {'form':form})
