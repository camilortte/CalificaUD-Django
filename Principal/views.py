#encoding:utf-8
#from Principal import models
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect ,render_to_response
from Principal.forms import LoginForm , ActualizarUserForm
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from Principal.models import Docente , Materia , Estudiante
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Principal.admin import UserCreationForm 



def index_general(request): 
    auth.logout(request)
    return render(request,'base_general.html')

@login_required(login_url='index_general')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index_private(request):
    return render_to_response('autenticado/index.html',context_instance=RequestContext(request))

def login(request):    
    auth.logout(request)
    if request.method == 'POST': 
        formulario = LoginForm(request.POST) 
        formularioRegistro = UserCreationForm() 
        if formulario.is_valid(): 
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('index_private',permanent=True)   
            else:         
                return render(request, 'register/login-register.html', 
                    {'formulario': formulario,'errorValidation':'Usuario o password Incorrectos','formularioRegistro': formularioRegistro,})
    else:
        formulario = LoginForm() 
        formularioRegistro = UserCreationForm() 
    return render(request, 'register/login-register.html', {'formulario': formulario,'formularioRegistro': formularioRegistro})

def logout(request):
    auth.logout(request)
    return redirect('home',permanent=True)


@login_required(login_url='index_general')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def todos_los_profesores(request):
    """docentes = Docente.objects.all()
    materias_docente=[]
    for docente in docentes:        
        materias_docente.append(Materia.objects.filter(profesor=docente))

    return render(request,'autenticado/todos_profesores.html',{'materias_docente':materias_docente})"""
    docentes = Docente.objects.all()
    return render(request,'autenticado/todos_profesores.html',{'docentes':docentes})
   

def registration(request):
    auth.logout(request)
    if request.method == 'POST': 
        formulario = LoginForm() 
        formularioRegistro =UserCreationForm(request.POST) 
        if formularioRegistro.is_valid():     
            formularioRegistro.save()
            return redirect('index_general')
    else:
        formulario = LoginForm() 
        formularioRegistro = UserCreationForm(request.POST)  # An unbound form
    return render(request, 'register/login-register.html', 
        {'formularioRegistro': formularioRegistro,'formulario': formulario,'registro':True})

   
@login_required(login_url='index_general')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def actualizar(request):
    if request.method == 'POST':    
        formulario = ActualizarUserForm(request.POST,instance=request.user)             
        if formulario.is_valid():      
            try:                  
                formulario.clean_password()
                password=formulario.cleaned_data['password1']        
                formulario.save()
                user = Estudiante.objects.get(email__exact=request.user)
                user.set_password(password)
                user.save()
                return render(request, 'register/actualizar.html', {'formulario': formulario,'ok':'Sus datos se almacenaron satisfactoriamente.'})
            except Exception:               
                return render(request, 'register/actualizar.html', 
                {'formulario': formulario,'user':request.user,'error':'Password no coincide.'})
    else:
        formulario = ActualizarUserForm(instance=request.user)     
    return render(request, 'register/actualizar.html', {'formulario': formulario,'user':request.user})

