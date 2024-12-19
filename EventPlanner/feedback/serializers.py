# feedback serializers
from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Read-only user field

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'event', 'comment', 'rating', 'created_at', 'updated_at']
