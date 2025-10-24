from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/formulario_producto.html', {
        'form': form, 
        'titulo': 'Crear Producto'
    })

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', producto_id=producto.id_producto)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/formulario_producto.html', {
        'form': form, 
        'titulo': 'Editar Producto'
    })

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'productos/confirmar_borrar.html', {'producto': producto})