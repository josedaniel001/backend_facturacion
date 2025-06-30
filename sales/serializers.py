# sales/serializers.py
from rest_framework import serializers
from .models import Sale, SaleItem
from customers.models import Customer
from inventory.models import Presentation

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', required=False, allow_null=True
    )

    class Meta:
        model = Sale
        fields = ['id', 'customer_id', 'customer_name', 'payment_method', 'status', 'total', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sale = Sale.objects.create(**validated_data)

        for item in items_data:
            SaleItem.objects.create(sale=sale, **item)

            # Actualiza stock de ProductPresentation
            pp = Presentation.objects.get(
                product=item['product'],
                size=item['size']
            )
            pp.stock -= item['quantity']
            pp.save()

        return sale
