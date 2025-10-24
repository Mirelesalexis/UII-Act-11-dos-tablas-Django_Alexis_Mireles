from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id_producto', 'nombre_producto', 'categoria', 'precio', 'stock', 'id_proveedor']
    list_filter = ['categoria', 'id_proveedor']
    search_fields = ['nombre_producto', 'descripcion']
    list_per_page = 20