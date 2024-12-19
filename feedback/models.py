# feedback/models.py
from django.db import models
from django.conf import settings
from events.models import Event  # Assuming you have an Event model in the events app

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedbacks')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField()  # Feedback text
    rating = models.PositiveSmallIntegerField()  # 1 to 5 rating
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback by {self.user.username} for {self.event.name}"
