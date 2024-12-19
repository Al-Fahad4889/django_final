from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/<int:transaction_id>/', views.TransactionDetailView.as_view(), name='transaction-detail'),
]
