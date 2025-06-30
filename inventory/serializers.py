from rest_framework import serializers
from .models import Product, Presentation,CategoriaProducto,Supplier

class PresentationSerializer(serializers.ModelSerializer):
    minStock = serializers.IntegerField(source='min_stock')
    class Meta:
        model = Presentation
        fields = ['id', 'size', 'price', 'stock', 'minStock']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=CategoriaProducto.objects.all())  # Devuelve nombre de categoría
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())  # Devuelve nombre de proveedor
    presentations = PresentationSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'supplier', 'status', 'presentations']

    def create(self, validated_data):
        presentations_data = validated_data.pop('presentations')
        product = Product.objects.create(**validated_data)
        for pres_data in presentations_data:
            Presentation.objects.create(product=product, **pres_data)
        return product

    def update(self, instance, validated_data):
        presentations_data = validated_data.pop('presentations', [])
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        # Borrar presentaciones previas y volver a crear (simple)
        instance.presentations.all().delete()
        for pres_data in presentations_data:
            Presentation.objects.create(product=instance, **pres_data)

        return instance
