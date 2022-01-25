from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    email = models.EmailField()
    
    def _str_(self):
        return f"Cliente {Cliente.nombre} {Cliente.apellido} {Cliente.email}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    cuil = models.IntegerField()
    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    codigo = models.IntegerField()
    precio = models.FloatField()
    cantidad = models.IntegerField()