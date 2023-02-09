from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from ..forms import LoginForm, SignUpForm
def signin(request):
    """
    Si el método de solicitud es GET, represente la plantilla signin.html con un formulario de
    autenticación. Si el método de solicitud es POST, autentique al usuario y, si el usuario está
    autenticado, inicie sesión y rediríjalo al panel.
    
    :param request: El objeto de solicitud es el primer parámetro de cada función de vista. Contiene
    información sobre la solicitud que se realizó al servidor, como el método HTTP, la URL, los
    encabezados y el cuerpo de la solicitud
    :return: El usuario está siendo devuelto.
    """
    if request.method == 'GET':
        return render(request, 'auth/signin.html', {"form": LoginForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth/signin.html', {"form": LoginForm, "error": "Usuario o contraseña incorrecta"})

        login(request, user)
        return redirect('dashboard')
    
def dashboard(request):
    return render(request, 'auth/dashboard.html')

def signup(request):
    """
    Si el método de solicitud es GET, presente la plantilla signup.html con UserCreationForm.
    
    Si el método de solicitud es POST, compruebe si las contraseñas coinciden. Si es así, cree un nuevo
    usuario y guárdelo en la base de datos. Si las contraseñas no coinciden, presente la plantilla
    signup.html con UserCreationForm y un mensaje de error.
    
    :param request: El objeto de solicitud es un objeto de Python que contiene información sobre la
    solicitud HTTP actual
    :return: un objeto de renderizado.
    """
    if request.method == 'GET':
        return render(request, 'auth/signup.html', {"form": SignUpForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'signup.html', {"form": SignUpForm, "error": "El nombre de usuario ya está en uso."})
        else:
            return render(request, 'signup.html', {"form": SignUpForm, "error": "Las contraseñas no coinciden."})

@login_required
def signout(request):
    logout(request)
    return redirect('signin')
