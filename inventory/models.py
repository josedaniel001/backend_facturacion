from django.db import models
from suppliers.models import Supplier  # Ajusta el import según tu estructura
from catalogos.models import CategoriaProducto  # Ajusta también

class Product(models.Model):
    STATUS_CHOICES = [
        ("active", "Activo"),
        ("inactive", "Inactivo"),
        ("low_stock", "Stock Bajo"),
        ("out_of_stock", "Sin Stock"),
    ]

    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return self.name


class Presentation(models.Model):
    product = models.ForeignKey(Product, related_name="presentations", on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    min_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.size} - {self.product.name}"
