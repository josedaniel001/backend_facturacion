from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'contact_person', 'email', 'phone', 'status',
        'registration_date', 'last_order', 'total_orders'
    )
    search_fields = ('name', 'contact_person', 'email')
    filter_horizontal = ('categories',)
