from django.forms import FloatField, Form, CharField, ImageField, IntegerField, EmailField

class ProductosForm(Form):
    Nombre = CharField()
    codigo = IntegerField()
    
class ClientesForm(Form):
    nombre = CharField()
    apellido = CharField()
    email = EmailField()
    dni = IntegerField()
    
class CargaproductosForm(Form):
    nombre = CharField(max_length=30)
    marca = CharField(max_length=30)
    codigo = IntegerField()
    precio = FloatField()
    cantidad = IntegerField()
    
class Cargaproveedores(Form):
    nombre = CharField(max_length=50)
    cuil = IntegerField()
    provincia = CharField(max_length=30)
    
class AvatarFormulario(Form):
    imagen = ImageField(required = True)