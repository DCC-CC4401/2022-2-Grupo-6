
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_inicial.models import User
from django.contrib.auth import authenticate, login,logout


def index(request):
    return render(request,"registration/index.html")

def register_user(request):
    if request.method == 'GET': #Si estamos cargando la página
     return render(request, "registration/register_user.html") #Mostrar el template

    elif request.method == 'POST': #Si estamos recibiendo el form de registro
        #Tomar los elementos del formulario que vienen en request.POST
        nombre = request.POST['nombre']
        contrasena = request.POST['contrasena']
        mail = request.POST['correo']

        #Crear el nuevo usuario
        user = User.objects.create_user(username=nombre, password=contrasena, email=mail)

        #Redireccionar la página /tareas
        return HttpResponseRedirect('/registration/home')

def login_user(request):
    if request.method == 'GET':
        return render(request,"registration/login.html")  
    if request.method == 'POST':
        username = request.POST['nombre']
        contrasena = request.POST['contrasena']
        usuario = authenticate(username=username,password=contrasena)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/registration/home')
        else:
            return HttpResponseRedirect('/accounts/register')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def home(request):
    return render(request,"registration/home.html")


def profile(request):
    
    return render(request,"registration/profile.html")


def edit_profile(request):
    return render(request, "registration/edit_profile.html")