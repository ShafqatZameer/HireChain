from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Follows Single Responsibility Principle - handles user authentication and profile.
    """
    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('admin', 'Admin'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='job_seeker')
    phone = models.CharField(max_length=15, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'custom_users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    def is_admin_user(self):
        """Check if user is an admin"""
        return self.user_type == 'admin' or self.is_superuser
