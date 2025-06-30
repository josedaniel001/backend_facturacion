from django.db import models

class Customer(models.Model):
    CUSTOMER_TYPES = [
        ('mayorista', 'Mayorista'),
        ('minorista', 'Minorista'),
    ]

    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('inactive', 'Inactivo'),
        ('suspended', 'Suspendido'),
    ]

    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='minorista')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    registration_date = models.DateField(auto_now_add=True)
    last_purchase = models.DateField(null=True, blank=True)
    total_purchases = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    current_debt = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
