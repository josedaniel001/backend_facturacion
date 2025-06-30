from rest_framework import viewsets,filters
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # O ajusta a tu lógica de permisos
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__nombre', 'supplier__name']
