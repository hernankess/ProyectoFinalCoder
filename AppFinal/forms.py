from email import charset
from tkinter.tix import Form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import EmailField, CharField, ImageField, PasswordInput
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Repetir contraseña", widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:'' for k in fields}

class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Repetir contraseña", widget=PasswordInput)
    last_name = CharField()
    first_name = CharField()
    
    class Meta:
        model = User
        fields = ["email", "password1", "password2","first_name", "last_name"]
        help_texts = {k:'' for k in fields}