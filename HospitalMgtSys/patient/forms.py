from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    role = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'radio-select'}), choices=((2,"patient"),(3,"doctor")))
    # role1 = forms.ChoiceWidget(attrs= (), choices=((1,"Patient"),(2,"Doctor")))

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = '__all__'
        
class TreatmentForm(forms.ModelForm):
    
    class Meta:
        model = Treatment
        fields = '__all__'