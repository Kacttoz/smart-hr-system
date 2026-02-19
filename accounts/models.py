from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('MAIN_ADMIN', 'Main Admin'),
        ('SUB_ADMIN', 'Sub Admin'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='SUB_ADMIN')
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
    @property
    def is_main_admin(self):
        return self.role == 'MAIN_ADMIN'
    
    @property
    def is_sub_admin(self):
        return self.role == 'SUB_ADMIN'
