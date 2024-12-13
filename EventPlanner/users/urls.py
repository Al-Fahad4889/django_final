from django.urls import path
from .views import UserListCreateView, UserDetailView, ProfileDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/profile/', ProfileDetailView.as_view(), name='profile-detail'),
]
