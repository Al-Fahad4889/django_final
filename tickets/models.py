from django.db import models
from events.models import Event  # Assuming Event model is in the 'events' app

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)  # Primary key for the Ticket
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # ForeignKey to the Event model
    event_name = models.CharField(max_length=255)  # Name of the Event
    event_time = models.DateTimeField()  # Time of the Event

    def __str__(self):
        return f"Ticket {self.ticket_id} for {self.event_name} at {self.event_time}"
