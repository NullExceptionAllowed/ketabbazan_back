from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)  
