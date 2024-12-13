from django.urls import path
from .views import FeedbackListCreateView, FeedbackDetailView

urlpatterns = [
    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),
]
