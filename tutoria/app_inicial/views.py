
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_inicial.models import User
from app_inicial.models import Publicacion
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


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
    publicaciones = Publicacion.objects.all()
    return render(request,"registration/home.html",{'publicaciones':publicaciones})


def profile(request):
    return render(request,"registration/profile.html")



def publicaciones(request):
    # tenemos que hacer la funcion para ingresar los datos a la base de datos y para mostrarlos
    if request.method == 'GET':
        return render(request,"registration/create_publicaciones.html")
    
    elif request.method == 'POST':
        
        titulo = request.POST['title']
        subject = request.POST['subject']
        schedule = request.POST['schedule']
        cost = request.POST['cost']
        descripcion = request.POST['descripcion']
        
        publicacion = Publicacion.objects.create(descripcion=descripcion, titulo=titulo, subject=subject, schedule=schedule, cost=cost, owner=request.user)
        publicacion.save()
        messages.success(request,'buenas noches tengo caña afasd')
        return HttpResponseRedirect('registration/home.html')
