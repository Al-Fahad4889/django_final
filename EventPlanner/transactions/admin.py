from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'price', 'user', 'buyer_name', 'buyer_phone', 'date')
    search_fields = ('buyer_name', 'buyer_phone')
    list_filter = ('date',)
