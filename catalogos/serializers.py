from rest_framework import serializers
from .models import CategoriaProducto, Pais, Departamento, Municipio

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ['id', 'nombre', 'descripcion']

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre']

class DepartamentoSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()

    class Meta:
        model = Departamento
        fields = ['id', 'nombre', 'pais']

class MunicipioSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()

    class Meta:
        model = Municipio
        fields = ['id', 'nombre', 'departamento']
