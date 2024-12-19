from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, logout
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer

# API view for user registration
class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]  # Allow anyone to register
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Save the new user instance
        serializer.save()

# API view for login
class LoginView(ObtainAuthToken):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(user=self.object)
        response.data['token'] = token.key  # Attach the token to the response
        return response

# API view for logout
class LogoutView(generics.APIView):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can log out

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()  # Delete the user's token
        logout(request)  # Log out the user
        return Response({'message': 'Logged out successfully.'})

# API view for retrieving, updating, and deleting a user's profile
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access their profile
    serializer_class = ProfileSerializer

    def get_object(self):
        # Get the profile of the logged-in user
        return self.request.user.profile

    def get(self, request, *args, **kwargs):
        """
        Retrieve the current user's profile.
        Includes the user's username in the response.
        """
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        serializer_data = serializer.data
        serializer_data['username'] = request.user.username
        return Response(serializer_data)

    def put(self, request, *args, **kwargs):
        """
        Update the current user's profile.
        The user can modify fields like bio, location, phone number, etc.
        """
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)  # Allows partial updates
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """
        Delete the current user's profile.
        This will also delete the associated user account.
        """
        profile = self.get_object()
        profile.delete()
        request.user.delete()  # Deletes the associated user account
        return Response({'message': 'Profile and user account deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

# API view for admins to view a list of all users
class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]  # Only admins can access this
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
