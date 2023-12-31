# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    last_login = models.DateTimeField(null=True, blank=True)
