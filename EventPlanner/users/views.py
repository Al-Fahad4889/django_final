from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.views import View

class UserListView(View):
    def get(self, request):
        users = User.objects.all().values('user_id', 'name', 'email', 'is_attendee', 'is_organizer', 'is_admin')
        return JsonResponse(list(users), safe=False)

class UserCreateView(View):
    def post(self, request):
        data = request.POST
        user = User.objects.create_user(
            email=data['email'],
            name=data['name'],
            password=data['password'],
            is_attendee=data.get('is_attendee', False),
            is_organizer=data.get('is_organizer', False),
            is_admin=data.get('is_admin', False),
        )
        return JsonResponse({'message': 'User created successfully', 'user_id': user.user_id})
