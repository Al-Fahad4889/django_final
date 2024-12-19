from django.db import models
from users.models import User
from events.models import Event

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    msg = models.CharField(max_length=500)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"Notification for {self.user.name} about {self.event.name}"
