from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionCreateView.as_view(), name='transaction-create'),  # POST - Create a transaction
    path('all/', views.TransactionListView.as_view(), name='transaction-list'),  # GET - List all transactions
    path('<int:transaction_id>/', views.TransactionDetailView.as_view(), name='transaction-detail'),  # GET - Transaction details
    path('<int:transaction_id>/delete/', views.TransactionDeleteView.as_view(), name='transaction-delete'),  # DELETE - Delete a transaction
]
