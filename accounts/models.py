from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank =True)
    Ta_Classes = models.CharField(max_length=100,blank=True, null=True)
    Days = models.CharField(max_length=50)
    Hours = models.CharField(max_length=50)
    Bio = models.CharField(max_length=200)

    
    # Create your models here.
