from rest_framework import serializers
from .models import User, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_attendee', 'is_organizer', 'is_admin']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'location', 'phone']
