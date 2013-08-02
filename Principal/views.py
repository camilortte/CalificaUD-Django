#encoding:utf-8
#from Principal import models
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect ,render_to_response
from Principal.forms import LoginForm , ActualizarUserForm ,ChangePasswordForm ,UserCreationForm , SeleccionFacultadesForm
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from Principal.models import Docente ,  Estudiante , Materia, Facultad , Carrera
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



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
                formulario.save()
                return render(request, 'register/actualizar.html', {'formulario': formulario,'ok':'Sus datos se almacenaron satisfactoriamente.'})
            except Exception:               
                return render(request, 'register/actualizar.html', 
                {'formulario': formulario,'user':request.user,'error':'Password no coincide.'})
    else:
        formulario = ActualizarUserForm(instance=request.user)     
    return render(request, 'register/actualizar.html', {'formulario': formulario,'user':request.user})

@login_required(login_url='index_general')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def change_password(request):
    if request.method=='POST':
        formulario= ChangePasswordForm(request.POST)
        if formulario.is_valid():
            try:
                password=formulario.cleaned_data['pasword_anterior']
                user = auth.authenticate(username=request.user, password=password)
                if user == None:
                    return render(request, 'register/change_password.html', 
                    {'formulario': formulario,'user':request.user,'error':'Password anterior no coincide.'})   
                else:
                    user = Estudiante.objects.get(email__exact=request.user)
                    password=formulario.cleaned_data['password1']
                    user.set_password(password)
                    user.save()
                    print "SE CAMBIO EL PASSWORD"
                    return render(request, 'register/change_password.html', 
                        {'formulario': formulario,'ok':'se cabmio la contraseña correctamente'})
            except Exception,e:
                return render(request, 'register/change_password.html', 
                    {'formulario': formulario,'user':request.user,'error':str(e)})
    else:
        formulario= ChangePasswordForm()
    return render(request, 'register/change_password.html', {'formulario':formulario})

@login_required(login_url='index_general')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def calificar(request):
    if request.method=='POST':        
        formulario=SeleccionFacultadesForm(request.POST)        
        if formulario.is_valid():
            facultad=formulario.cleaned_data['facultades']
            if facultad!=None:
                formulario.fields['carreras'].queryset=Carrera.objects.filter(facultad=Facultad.objects.filter(nombre=facultad))                
                carreras=formulario.cleaned_data['carreras']                
                if carreras != None:
                    formulario.fields['materias'].queryset=Materia.objects.filter(carrera=carreras)   
                    materia=formulario.cleaned_data['materias']
                    if materia!= None:
                        formulario.fields['docentes'].queryset=Docente.objects.filter(materia=Materia.objects.filter(nombre=materia))   
                    else:
                        del formulario.fields['docentes']    
                else:                    
                    del formulario.fields['materias']
                    del formulario.fields['docentes']
            else:
                del formulario.fields['carreras']
                del formulario.fields['materias']
                del formulario.fields['docentes']


        else:     
            del formulario.fields['carreras']
            del formulario.fields['materias']
            del formulario.fields['docentes']       
            return render(request,'autenticado/calificar.html',{'formulario':formulario})
    else:
        formulario=SeleccionFacultadesForm()
        del formulario.fields['carreras']
        del formulario.fields['materias']
        del formulario.fields['docentes']

    return render(request,'autenticado/calificar.html',{'formulario':formulario})
            


