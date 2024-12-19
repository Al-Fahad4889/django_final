from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotificationCreateView.as_view(), name='notification-create'),  # POST - Create a notification
    path('list/', views.NotificationListView.as_view(), name='notification-list'),  # GET - List notifications for the authenticated user
    path('<int:id>/', views.NotificationDetailView.as_view(), name='notification-detail'),  # GET - Retrieve a specific notification
    path('<int:id>/delete/', views.NotificationDeleteView.as_view(), name='notification-delete'),  # DELETE - Delete a notification
]
