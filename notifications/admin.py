from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'sent_at', 'type', 'msg')
    search_fields = ('msg', 'type', 'user__name')
    list_filter = ('type', 'sent_at')
