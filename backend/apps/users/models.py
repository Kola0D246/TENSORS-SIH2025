from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.institutes.models import Institute, Department

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('HOD', 'HOD'),
        ('Faculty', 'Faculty'),
        ('Student', 'Student')
    ]
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"
