from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['id_proveedor', 'nombre', 'pais', 'telefono', 'email']
    list_filter = ['pais']
    search_fields = ['nombre', 'email']
    list_per_page = 20