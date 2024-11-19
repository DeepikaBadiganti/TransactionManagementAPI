from django.urls import path
from .views import TransactionListCreateView, TransactionDetailUpdateView

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view()),
    path('transactions/<int:transaction_id>/', TransactionDetailUpdateView.as_view()),
]
