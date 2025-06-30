from django.contrib import admin
from .models import Product, Presentation

# Inline para manejar presentaciones dentro del producto
class PresentationInline(admin.TabularInline):
    model = Presentation
    extra = 1  # Muestra 1 fila extra para agregar más presentaciones

# Registro principal del modelo Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier', 'status')
    search_fields = ('name',)
    list_filter = ('category', 'supplier', 'status')
    inlines = [PresentationInline]  # Esto hace que puedas añadir presentaciones desde el producto
