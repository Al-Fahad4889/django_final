from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(models.Model):
    # Roles of users
    ROLE_CHOICES = [
        ('organizer', 'Organizer'),
        ('attendee', 'Attendee'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='attendee')  # Role assigned to the user
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True) # short description of user
    location = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True)  # Store links to social accounts
    preferences = models.JSONField(default=dict, blank=True)  # Store user preferences
