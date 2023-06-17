from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=256, null=True)
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
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    present_treatment = models.CharField(max_length=256, null=True)
    start_date =models.DateTimeField()
    duration = models.DurationField()
    prescription = models.CharField(max_length=256, null=True)
    # reports = 

    def __str__(self):
        return self.present_treatment