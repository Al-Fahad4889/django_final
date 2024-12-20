from django.urls import path
from .views import EventListCreateView, EventDetailView, EventApproveView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:pk>/approve/', EventApproveView.as_view(), name='event-approve'),
]
