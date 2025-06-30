from django.db import models
from catalogos.models import CategoriaProducto

class Supplier(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    # Cambiado de FK a ManyToMany
    categories = models.ManyToManyField(
        CategoriaProducto,
        related_name='suppliers'
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    registration_date = models.DateField(auto_now_add=True)
    last_order = models.DateField(blank=True, null=True)
    total_orders = models.PositiveIntegerField(default=0)
    total_purchases = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    payment_terms = models.CharField(max_length=100, default='30 días')
    rating = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
