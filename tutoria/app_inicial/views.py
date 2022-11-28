
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app_inicial.models import User, Oferta
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .forms import CrearOferta

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

        # chequeamos si no está en la lista
        query_1 = User.objects.filter(username=nombre)
        query_2 = User.objects.filter(email=mail)
        bad = False
        print(request)
        if len(query_1) > 0:
            bad = True
        if len(query_2) > 0:
            bad = True
        if bad:

            return render(request, "registration/register_user.html")
        #Crear el nuevo usuario
        user = User.objects.create_user(username=nombre, password=contrasena, email=mail)
        messages.success(request,"Tu cuenta a sido creada coccn exito")
        #Redireccionar la página /tareas
        return HttpResponseRedirect('/accounts/home')

def login_user(request):
    if request.method == 'GET':
        return render(request,"registration/login.html")  
    if request.method == 'POST':
        email = request.POST['email']
        contrasena = request.POST['contrasena']

        query = User.objects.filter(email=email)
        # supone que solo hay uno en la base de datos, sino hay un bug
        username = query[0].username
        usuario = authenticate(username=username,password=contrasena)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/accounts/home')
        else:
           
            return HttpResponseRedirect('/accounts/login')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return redirect('index')

def home(request):
    if request.user.is_authenticated:
        return render(request,"registration/home.html")

    else:
        return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user
        }
        return render(request,"registration/profile.html",context)
    else:
        return redirect('login')



def crear_oferta(request):
     if request.user.is_authenticated:
        form = CrearOferta()
        if request.method == "POST":
            form = CrearOferta(request.POST)
            if form.is_valid():
                oferta = form.save(commit=False)
                oferta.p_user = request.user
                oferta.save()
                return redirect('ofertas_detail', pk=oferta.pk)
        else:
            form = CrearOferta()
        return render(request, 'registration/ofertaForm.html', {'form': form})
     else:
        return redirect('login')
    

def oferta_detail(request, pk):
    
    if request.user.is_authenticated:
        oferta_a = get_object_or_404(Oferta, pk=pk)
        return render(request, 'registration/oferta_list.html', {'oferta_a': oferta_a})
    else:
        return redirect('login')




def resumen(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            ofert = Oferta.objects.filter() 
            return render(request, 'registration/home.html', {'ofert' :ofert})
    else:
        return redirect('login')