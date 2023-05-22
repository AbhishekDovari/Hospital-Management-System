from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']