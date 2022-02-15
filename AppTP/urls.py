from unicodedata import name
from django.urls import path
from AppTP import views
from AppTP.views import buscar, busquedaproducto

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes', views.clientes, name="Clientes"),
    path('proveedor', views.ProveedoresListView.as_view(), name="Proveedores"),
    path("proveedor/add", views.ProveedoresCreateView.as_view(), name = "Proveedor_add"),
    path("proveedor/update/<pk>", views.ProveedoresUpdateView.as_view(), name = "Proveedor_update"),
    path("proveedor/delete/<pk>", views.ProveedoresDeleteView.as_view(), name = "Proveedor_delete"),
    path("proveedor/Detail/<pk>", views.ProveedoresDetailView.as_view(), name = "Proveedor_detail"),  
    path('producto', views.productos, name="Productos"),
    path("formulario_clientes", views.formulariocliente, name="Formulario_clientes"),
    path("busquedaproducto", views.busquedaproducto, name="Busquedaproducto"),
    path("buscar", views.buscar, name="Buscar"),
    path("formulario_carga_producto", views.formulariocargaproducto, name="Formulario_carga_producto"),
    path("producto_delete/<id_producto>", views.producto_delete, name= "Producto_delete"),
    path("producto_update/<id_producto>", views.producto_update, name= "Producto_update"),
    ]