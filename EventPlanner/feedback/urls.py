from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback/event/<int:event_id>/', views.FeedbackEventView.as_view(), name='feedback-event'),
    path('feedback/user/<int:user_id>/', views.FeedbackUserView.as_view(), name='feedback-user'),
]
