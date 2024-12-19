from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_attendee = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True,blank=True,default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
