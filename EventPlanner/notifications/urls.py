from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotificationCreateView.as_view(), name='notification-create'),
    path('user/<int:user_id>/', views.NotificationListView.as_view(), name='notification-list'),
    path('<int:notification_id>/', views.NotificationDetailView.as_view(), name='notification-detail'),
]
