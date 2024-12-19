from django.db import models
from users.models import User
from events.models import Event

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")  # User receiving the notification
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True, related_name="notifications")  # Related event
    sent_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the notification was sent
    msg = models.CharField(max_length=255)  # Notification message
    type = models.CharField(max_length=50, choices=[('info', 'Info'), ('alert', 'Alert'), ('warning', 'Warning')])  # Type of notification

    def __str__(self):
        return f"Notification to {self.user.name}: {self.msg}"
