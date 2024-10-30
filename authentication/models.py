from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
        (GUEST, 'Guest'),
    ]

    full_name = models.CharField(max_length = 100, null = False)
    email = models.EmailField(null = False , unique = True)
    phone_number = models.CharField(max_length = 15, null = False, unique = True)
    verifyPinPhone = models.CharField(max_length = 6, null = True)
    verifyPinEmail = models.CharField(max_length = 6, null = True)
    emailIsVerified = models.BooleanField(default = False)  
    phoneIsVerified = models.BooleanField(default = False)  
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    last_login = models.DateTimeField(default = timezone.now, null = False)
    role = models.CharField(max_length = 5, choices = ROLE_CHOICES, default = USER)


    
