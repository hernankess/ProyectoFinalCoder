from django.forms import Form, CharField, IntegerField, EmailField

class ProductosForm(Form):
    Nombre = CharField()
    codigo = IntegerField()
    
class ClientesForm(Form):
    nombre = CharField()
    apellido = CharField()
    email = EmailField()
    dni = IntegerField()