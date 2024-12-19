from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated

# Create a new ticket
class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]  # Require authentication to create tickets

# List all tickets for a specific event
class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return self.queryset.filter(event_id=event_id)

# Retrieve details of a specific ticket
class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'ticket_id'

# Delete a specific ticket
class TicketDeleteView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'ticket_id'
