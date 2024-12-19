from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:user_id>/profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('profile/<int:user_id>/', views.UserProfileDetailView.as_view(), name='user-profile-detail'),
]
