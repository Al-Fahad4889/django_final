from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.permissions import IsAuthenticated

class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

class FeedbackEventView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return self.queryset.filter(event_id=event_id)

class FeedbackUserView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return self.queryset.filter(user_id=user_id)
