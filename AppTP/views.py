import email
from re import I
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppTP.models import Producto, Proveedor, Cliente
from AppTP.forms import ProductosForm, ClientesForm
from AppTP.forms import ProductosForm

# Create your views here.

def inicio(request):
    
      return render(request, "AppTP/inicio.html")
  
def clientes(request):
    
      return render(request, "AppTP/clientes.html", {"Cliente": Cliente.objects.all()})
  
def productos(request):
    
      return render(request, "AppTP/productos.html")
  
def proveedores(request):
    
      return render(request, "AppTP/proveedores.html")

def formulariocliente(request):
    
      if request.method == "POST":
      
            formulario_cliente = ClientesForm(request.POST) 
            
            if formulario_cliente.is_valid():
                  data= formulario_cliente.cleaned_data
                  Cliente.objects.create(nombre=data["nombre"], apellido=data["apellido"], email=data["email"],dni=data["dni"])
                  return redirect("Clientes")
      else:
            formulario_cliente = ClientesForm()

      return render(request, "AppTP/formulario_clientes.html", {"formulario_cliente":formulario_cliente})
  
  
def busquedaproducto(request):
      return render(request, "AppTP/busquedaproducto.HTML")
  
def buscar(request):
    
    if request.GET["codigo"]:
        codigo = request.GET["codigo"]
        nombre = Producto.objects.filter(codigo=codigo)
        marca = Producto.objects.filter(codigo=codigo)
        precio = Producto.objects.filter(codigo=codigo)
        cantidad = Producto.objects.filter(codigo=codigo)
        
        return render(request, "AppTP/resultadobusqueda.html", {"nombre":nombre, "marca":marca, "cantidad":cantidad, "precio":precio})
    
    else:
        
        respuesta = "No ingresaste Datos"
    
    return HttpResponse(respuesta)