from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor
from .forms import ProveedorForm

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/listar_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
    productos = proveedor.productos.all()
    return render(request, 'proveedores/detalle_proveedor.html', {
        'proveedor': proveedor,
        'productos': productos
    })

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores:listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/formulario_proveedor.html', {
        'form': form, 
        'titulo': 'Crear Proveedor'
    })

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores:detalle_proveedor', proveedor_id=proveedor.id_proveedor)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/formulario_proveedor.html', {
        'form': form, 
        'titulo': 'Editar Proveedor'
    })

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores:listar_proveedores')
    return render(request, 'proveedores/confirmar_borrar_proveedor.html', {'proveedor': proveedor})