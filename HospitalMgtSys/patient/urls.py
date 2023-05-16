from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('patient/', views.patient),
    path('doctor/', views.doctor),    
]