from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('events/<int:event_id>/', views.EventDetailView.as_view(), name='event-detail'),
    path('events/<int:event_id>/approve/', views.EventApproveView.as_view(), name='event-approve'),
]
