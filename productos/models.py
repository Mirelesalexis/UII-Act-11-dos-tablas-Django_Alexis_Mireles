from django.db import models
from proveedores.models import Proveedor

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre_producto

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre_producto']