from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    language_preference = models.CharField(max_length=10, default='en')
    
    def __str__(self):
        return self.email