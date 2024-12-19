from django.db import models
from users.models import User

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=255)
    price = models.IntegerField()
