from collections import UserDict
from msilib.schema import ListView
from re import M, template
import re
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def hospital(request):
    hospital_list = Hospital.objects.all()
    return render(request, 'hospital.html', {'hospital' : hospital_list})

def profesional(request):
    profesional_list = Profesional.objects.all()
    return render(request, 'profesional.html', {'profesional' : profesional_list})

def especialidad(request):
    especialidad_list = Especialidad.objects.all()
    return render(request, 'especialidad.html', {'especialidad' : especialidad_list})

def especialidadAgregar(request):
    if request.method == 'POST':
        miFormulario = EspecialidadAgregar(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        especialidad = Especialidad(nombre=nombre)
        especialidad.save()
        return render(request, 'index.html')
    else:
        miFormulario = EspecialidadAgregar()    
    return render(request, 'especialidadAgregar.html', {'miFormulario':miFormulario})

def profesionalBuscar(request):
    return render(request, 'profesionalBuscar.html')    

def profesionalBuscarResultado(request):
    if request.GET['especialidad']:
        especialidad = request.GET['especialidad']
        profesionales = Profesional.objects.filter(especialidad=especialidad)
        return render(request, 'profesionalBuscarResultado.html', {'profesionales': profesionales, 'especialidad': especialidad})
    else:
        respuesta = 'No se ha encontrado ningún profesional'
    return HttpResponse(respuesta)

def hospitalLeer(request):
    hospitales = Hospital.objects.all()
    contexto = {'hospitales':hospitales}
    return render(request, 'hospital.html', contexto)

def profesionalLeer(request):
    profesionales = Profesional.objects.all()
    contexto = {'profesionales':profesionales}
    return render(request, 'profesional.html', contexto)

def profesionalEliminar(request, apellido):
    profesional = Profesional.objects.get(apellido=apellido)
    profesional.delete()
    profesionales = Profesional.objects.all()
    contexto = {'profesionales': profesionales}
    return render(request, 'profesional.html', contexto)

def profesionalEditar(request, matrícula):
    profesional = Profesional.objects.get(matrícula=matrícula)
    if request.method == 'POST':
        miFormulario = ProfesionalEditar(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesional.nombre = informacion['nombre']
            profesional.apellido = informacion['apellido']
            profesional.edad = informacion['edad']
            profesional.email = informacion['email']
            profesional.save()
            profesionales = Profesional.objects.all()
            contexto = {'profesionales': profesionales}
            return render(request, 'profesional.html', contexto)
    else:
        miFormulario = ProfesionalEditar(initial={'nombre': profesional.nombre, 'apellido': profesional.apellido, 'edad': profesional.edad, 'email': profesional.email})
        contexto = {'miFormulario':miFormulario, 'matrícula':matrícula}
        return render(request, 'profesionalEditar.html', contexto)

class ProfesionalList(LoginRequiredMixin, ListView):
    model = Profesional
    template_name = 'profesional.html'

@login_required
class ProfesionalDetalle(DetailView):
    model = Profesional
    success_url = reverse_lazy('Profesional')
    fields = ['nombre', 'apellido', 'edad', 'matrícula', 'especialidad', 'hospital']

@login_required
class ProfesionalCrear(CreateView):
    model = Profesional
    success_url = reverse_lazy('Profesional')
    fields = ['nombre', 'apellido', 'edad', 'email', 'matrícula', 'especialidad', 'hospital']

@login_required
class ProfesionalEdicion(UpdateView):
    model = Profesional
    success_url = reverse_lazy('Profesional')
    fields = ['nombre', 'apellido', 'edad', 'email', 'matrícula', 'especialidad', 'hospital']

@login_required
class ProfesionalEliminar(DeleteView):
    model = Profesional
    success_url = reverse_lazy('Profesional')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request,user)
                return render(request, 'index.html', {'msg':f'Bienvenido de nuevo, {usuario}'})
            else:
                return render(request, 'index.html', {'msg':'El usuario o la contraseña son incorrectos'})
        else:
            return render(request, 'index.html', {'msg':'El usuario o la contraseña son incorrectos'})
    else:
        form  = AuthenticationForm()
        return render(request, 'login.html', {'form': form})    

def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'index.html', {'msg':f'Bienvenido/a {username}, te has registrado exitosamente!'})
        else:
            return render(request, 'index.html', {'msg':'Error: el usuario no ha podido ser creado'}) 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})