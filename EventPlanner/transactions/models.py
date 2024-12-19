from django.db import models
from users.models import User
from events.models import Event

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)  # Primary Key
    price = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="transactions")  # ForeignKey to Event for price
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")  # ForeignKey to User
    buyer_name = models.CharField(max_length=100)  # Buyer Name
    buyer_phone = models.CharField(max_length=15)  # Buyer Phone
    date = models.DateTimeField(auto_now_add=True)  # Transaction Date and Time (auto-generated)

    def __str__(self):
        return f"Transaction {self.transaction_id} by {self.buyer_name}"
