# feedback/urls.py
from django.urls import path
from .views import FeedbackListCreateView, FeedbackRetrieveUpdateDestroyView

urlpatterns = [
    path('', FeedbackListCreateView.as_view(), name='feedback-list-create'),  # List all or create feedback
    path('<int:pk>/', FeedbackRetrieveUpdateDestroyView.as_view(), name='feedback-detail'),  # Retrieve, update, delete
]
