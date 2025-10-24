from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'categoria', 'precio', 'stock', 'descripcion', 'imagen', 'id_proveedor']
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad en stock'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del producto'}),
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre_producto': 'Nombre del Producto',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'stock': 'Stock',
            'descripcion': 'Descripción',
            'imagen': 'Imagen del Producto',
            'id_proveedor': 'Proveedor',
        }