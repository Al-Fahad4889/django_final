from rest_framework import generics, permissions
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackListCreateView(generics.ListCreateAPIView):
    """
    Allows users to list all feedback for an event or create new feedback.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        # Filter feedback by event ID provided in the query parameters
        event_id = self.request.query_params.get('event')
        if event_id:
            return Feedback.objects.filter(event_id=event_id)
        return Feedback.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedbackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows users to retrieve, update, or delete a specific feedback.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        # Ensure users can only modify their own feedback
        return Feedback.objects.filter(user=self.request.user)
