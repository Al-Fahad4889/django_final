from django.db import models
from users.models import User
from events.models import Event

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    price = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_phone = models.CharField(max_length=15)
    date = models.DateTimeField()
