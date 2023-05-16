from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def patient(request):
    return render(request, 'authentication/patient.html')

def doctor(request):
    return render(request,'authentication/doctor.html')