from rest_framework import viewsets
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('-registration_date')
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
