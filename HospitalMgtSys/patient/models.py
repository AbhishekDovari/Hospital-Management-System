from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    

class Treatment(models.Model):
    # lp = User.objects.filter(groups = 2)
    # ld = User.objects.filter(groups = 3)
    # patient = models.ForeignKey(lp, null=True, on_delete=models.SET_NULL)
    # doctor = models.ForeignKey(ld, null=True, on_delete=models.SET_NULL)
    present_treatment = models.CharField(max_length=256, null=True)
    start_date =models.DateTimeField()
    duration = models.DurationField()
    prescription = models.CharField(max_length=256, null=True)
    # reports = 

    def __str__(self):
        return self.present_treatment

# class appointment(models.Model):



