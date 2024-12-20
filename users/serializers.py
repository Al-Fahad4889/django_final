from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')  # Include 'role'
        extra_kwargs = {
            'password': {'write_only': True},  # Password should be write-only
        }

    def create(self, validated_data):
        # Create a new user with the specified role and save it
        role = validated_data.pop('role', 'participant')  # Default to 'participant' if no role provided
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.role = role
        user.save()
        return user

# Serializer for Profile model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  # Include all fields in the profile
