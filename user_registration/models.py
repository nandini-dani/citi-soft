from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser): 
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=15, blank=False, unique=True)
    password = models.CharField(max_length=255)
    recovery_email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    registration_date = models.DateTimeField(auto_now_add=True, 
                                             editable=False)
    
    class Meta:
        ordering = ['registration_date']
        db_table = 'auth_user'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reversed('user-detail', args=[str(self.id)])
