from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaProductoViewSet,
    PaisViewSet,
    DepartamentoViewSet,
    MunicipioViewSet,
)

router = DefaultRouter()
router.register(r'categorias', CategoriaProductoViewSet)
router.register(r'paises', PaisViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'municipios', MunicipioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
