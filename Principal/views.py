#encoding:utf-8
#from Principal import models
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect ,render_to_response
from Principal.forms import LoginForm
from django.template import RequestContext
from django.views.decorators.cache import cache_control




def index_general(request): 
    auth.logout(request)
    return render(request,'base_general.html')

@login_required(login_url='index_general')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index_private(request):
    return render_to_response('base.html',context_instance=RequestContext(request))

def login(request):    
    auth.logout(request)
    if request.method == 'POST': 
        formulario = LoginForm(request.POST) 
        if formulario.is_valid(): 
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('index_private',permanent=True)   
            else:         
                return render(request, 'login.html', 
                    {'formulario': formulario,'errorValidation':'Usuario o password Incorrectos'})
    else:
        formulario = LoginForm() # An unbound form
    return render(request, 'login.html', {'formulario': formulario})

def logout(request):
    auth.logout(request)
    return redirect('home',permanent=True)

  



