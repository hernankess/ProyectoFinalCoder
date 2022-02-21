from django.db import models
from django.db.models import ForeignKey, CASCADE, Model, ImageField
from django.contrib.auth.models import User
from datetime import datetime

from django.forms import CharField, DateField

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f"Cliente {self.nombre} {self.apellido} DNI: {self.dni}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    cuil = models.IntegerField()
    provincia = models.CharField(max_length=30)
    
    def __str__(self):
            return f"Proveedor {self.nombre} {self.cuil} {self.provincia}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    codigo = models.IntegerField()
    precio = models.FloatField()
    cantidad = models.IntegerField()
    fecha_alta = models.CharField(max_length=100, null=True, blank=True, default=datetime.now())
    
    def __str__(self):
        return f"Producto {self.nombre} {self.marca} {self.codigo} {self.precio} {self.cantidad}, El producto se cargó el día {self.fecha_vencimiento}"
    
class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to="avatares", null=True, blank=True)