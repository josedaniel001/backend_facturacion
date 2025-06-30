from rest_framework import serializers
from .models import Supplier
from catalogos.models import CategoriaProducto

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ['id', 'nombre']
        
class SupplierSerializer(serializers.ModelSerializer):
    categories_names = serializers.SerializerMethodField()
    class Meta:
        model = Supplier
        fields = '__all__'

    def get_categories_names(self, obj):
        return [cat.nombre for cat in obj.categories.all()]