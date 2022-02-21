from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from platformdirs import user_cache_dir
from AppFinal.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data["username"]
            contrasena = form.cleaned_data["password"]
            
            user = authenticate(username=usuario , password=contrasena)
            
            if user is not None:
                login(request, user)
                return redirect("Inicio")
            else:
                return render(request, 'login.html', 
                    {'form': form,
                    'error': 'No es válido el usuario y contraseña'})
        else:
            return render(request, "login.html", {"form" : form})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form" : form})
        
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            # return render(request, "login.html", {"mensaje" : f'Usuario {username} creado correctamente!'})
            return HttpResponse (f'Usuario {username} creado correctamente!')
            
    else:
        form = UserRegisterForm()
    
    return render(request, "registro.html", {"form": form})

@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.save()
            
            return redirect ("Inicio")
    else:
        formulario = UserEditForm({"email": usuario.email})
    
    return render (request, "registro.html", {"form" : formulario})