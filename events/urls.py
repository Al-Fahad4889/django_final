from django.urls import path
from .views import EventListView, EventDetailView, EventStatusUpdateView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:pk>/status/', EventStatusUpdateView.as_view(), name='event-status-update'),
]
