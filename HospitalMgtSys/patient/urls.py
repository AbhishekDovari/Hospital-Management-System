from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('patient/', views.patient),
    path('doctor/', views.doctor),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='login'),
    path('logout/', views.logout_view, name='logout'),    
]