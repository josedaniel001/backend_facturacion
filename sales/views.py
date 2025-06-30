# sales/views.py
from rest_framework import generics
from .models import Sale
from .serializers import SaleSerializer

class SaleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sale.objects.all().order_by('-created_at')
    serializer_class = SaleSerializer
