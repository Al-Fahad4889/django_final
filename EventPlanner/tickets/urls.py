from django.urls import path
from . import views

urlpatterns = [
    path('', views.TicketCreateView.as_view(), name='ticket-create'),  # POST - Create a new ticket
    path('event/<int:event_id>/', views.TicketListView.as_view(), name='ticket-list'),  # GET - List all tickets for an event
    path('<int:ticket_id>/', views.TicketDetailView.as_view(), name='ticket-detail'),  # GET - Retrieve a specific ticket
    path('<int:ticket_id>/delete/', views.TicketDeleteView.as_view(), name='ticket-delete'),  # DELETE - Delete a ticket
]
