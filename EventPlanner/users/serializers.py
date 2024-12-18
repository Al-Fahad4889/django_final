from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')  # Include role for role-based access
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    def create(self, validated_data):
        # Create a new user with the given details and save it
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        return user

# Serializer for Profile model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  # Include all fields in the profile
