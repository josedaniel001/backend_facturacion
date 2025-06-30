from django.contrib import admin
from .models import Pais, Departamento, Municipio, CategoriaProducto

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais')
    search_fields = ('nombre',)
    list_filter = ('pais',)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'departamento')
    search_fields = ('nombre',)
    list_filter = ('departamento',)

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
