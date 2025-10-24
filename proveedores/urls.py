from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.listar_proveedores, name='listar_proveedores'),
    path('<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('crear/', views.crear_proveedor, name='crear_proveedor'),
    path('editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),
]