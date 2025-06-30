from django.db import models
from inventory.models import Product  # importa de tu app de productos
from customers.models import Customer

class Sale(models.Model):
    PAYMENT_METHODS = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    )
    STATUS_CHOICES = (
        ('completed', 'Completada'),
        ('pending', 'Pendiente'),
        ('cancelled', 'Cancelada'),
    )

    customer = models.ForeignKey(
            Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='sales'
        )
    customer_name = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Sale #{self.pk} - {self.customer_name}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)  # presentación
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.product.name} - {self.size} x {self.quantity}"
