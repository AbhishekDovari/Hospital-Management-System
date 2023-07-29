from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.patient, name='patient'),
    path('patient/<int:pk>/', views.patient_profile, name='patient_pro'),
    path('doctor/', views.doctor, name='doctor'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('patientform/', views.createPatient, name='patientform'),
    path('treatment/', views.treatment, name='treatment'),    
]