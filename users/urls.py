from django.urls import path
from .views import (
    RegisterView, 
    LoginView, 
    LogoutView, 
    ProfileDetailView, 
    UserListView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # User registration endpoint
    path('login/', LoginView.as_view(), name='login'),          # User login endpoint
    path('logout/', LogoutView.as_view(), name='logout'),       # User logout endpoint
    path('profile/', ProfileDetailView.as_view(), name='profile'),  # User profile detail endpoint
    path('admin/users/', UserListView.as_view(), name='admin-users'),  # List all users (admin only)
]
