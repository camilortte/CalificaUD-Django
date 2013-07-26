#encoding:utf-8
#from Principal import models
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect ,render_to_response
from Principal.forms import LoginForm,RegisterFormForm
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from Principal.models import Docente , Materia



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
        formularioRegistro = RegisterFormForm() 
        if formulario.is_valid(): 
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('index_private',permanent=True)   
            else:         
                return render(request, 'register/login.html', 
                    {'formulario': formulario,'errorValidation':'Usuario o password Incorrectos','formularioRegistro': formularioRegistro,})
    else:
        formulario = LoginForm() 
        formularioRegistro = RegisterFormForm() 
    return render(request, 'register/login.html', {'formulario': formulario,'formularioRegistro': formularioRegistro})

def logout(request):
    auth.logout(request)
    return redirect('home',permanent=True)

def registration(request):
    auth.logout(request)
    if request.method == 'POST': 
        formulario = LoginForm() 
        formularioRegistro = RegisterFormForm(request.POST) 
        if formularioRegistro.is_valid():     
            #userName = request.cleaned_data['username', None]
            #userPass = request.cleaned_data['password', None]
            #userMail = request.cleaned_data['email', None]
            #return render(request, 'login.html')
            return redirect('index_general')
    else:
        formulario = LoginForm() 
        formularioRegistro = RegisterFormForm() # An unbound form
    return render(request, 'register/login.html', {'formularioRegistro': formularioRegistro,'formulario': formulario,'registro':True})

@login_required(login_url='index_general')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def todos_los_profesores(request):
    docentes = Docente.objects.all()
    materias_docente=[]
    for docente in docentes:        
        materias_docente.append(Materia.objects.filter(profesor=docente))
    materias_docente=Materia.objects.filter(profesor__id=2)
    return render(request,'autenticado/todos_profesores.html',{'materias_docente':materias_docente})
   

   

