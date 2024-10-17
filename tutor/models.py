from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import CustomUser


def __str__(self):
    return f"{self.username}: is avalible at {self.Days} at {self.Hours}"