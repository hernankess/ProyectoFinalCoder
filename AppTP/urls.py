from unicodedata import name
from django.urls import path
from AppTP import views
from AppTP.views import buscar, busquedaproducto

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes', views.clientes, name="Clientes"),
    path('proveedor', views.proveedores, name="Proveedores"),
    path('producto', views.productos, name="Productos"),
    path("formulario_clientes", views.formulariocliente, name="Formulario_clientes"),
    path("busquedaproducto", views.busquedaproducto, name="Busquedaproducto"),
    path("buscar", views.buscar, name="Buscar"),
    ]