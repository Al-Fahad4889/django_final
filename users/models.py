from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Custom User model with roles and extended permissions
class User(AbstractUser):
    # Roles for the users
    ROLE_CHOICES = [
        ('organizer', 'Organizer'),
        ('attendee', 'Attendee'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='attendee')

    # To avoid conflicts, custom related names are added for groups and permissions
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions') 

# Profile model to store additional user information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # Links profile to a user
    bio = models.TextField(blank=True, null=True)  # Short description of the user
    location = models.CharField(max_length=255, blank=True, null=True)  # User's location
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # User's contact number
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Profile image
    social_links = models.JSONField(default=dict, blank=True)  # Social media links in JSON format
    preferences = models.JSONField(default=dict, blank=True)  # User preferences in JSON format
