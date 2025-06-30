from rest_framework import viewsets
from .models import CategoriaProducto, Pais, Departamento, Municipio
from .serializers import (
    CategoriaProductoSerializer,
    PaisSerializer,
    DepartamentoSerializer,
    MunicipioSerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoriaProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoriaProducto.objects.all().order_by('nombre')
    serializer_class = CategoriaProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PaisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pais.objects.all().order_by('nombre')
    serializer_class = PaisSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DepartamentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Departamento.objects.all().order_by('nombre')
    serializer_class = DepartamentoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MunicipioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Municipio.objects.all().order_by('nombre')
    serializer_class = MunicipioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
