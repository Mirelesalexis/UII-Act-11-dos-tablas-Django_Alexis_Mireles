from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, help_text="Nombre del proveedor")
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"