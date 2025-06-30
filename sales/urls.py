# sales/urls.py
from django.urls import path
from .views import SaleListCreateAPIView

urlpatterns = [
    path('', SaleListCreateAPIView.as_view(), name='sales-list-create'),
]
