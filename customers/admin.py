from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'email', 'phone', 'city', 'customer_type', 'status']
    search_fields = ['name', 'contact_person', 'email']
    list_filter = ['status', 'customer_type', 'city']
