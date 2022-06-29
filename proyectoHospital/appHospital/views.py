from msilib.schema import ListView
from re import M, template
import re
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class ProfesionalList(ListView):
    model = Profesional
    template_name = 'profesional.html'

class ProfesionalDetalle(DetailView):
    model = Profesional
    success_url = reverse_lazy('Profesional')
    fields = ['nombre', 'apellido', 'edad', 'matrícula', 'especialidad', 'hospital']

class ProfesionalCrear(CreateView):
    model = Profesional
    success_url = reverse_lazy('Profesional')
    fields = ['nombre', 'apellido', 'edad', 'email', 'matrícula', 'especialidad', 'hospital']

class ProfesionalEdicion(UpdateView):
    model = Profesional
    success_url = reverse_lazy('Profesional')
    fields = ['nombre', 'apellido', 'edad', 'email', 'matrícula', 'especialidad', 'hospital']

class ProfesionalEliminar(DeleteView):
    model = Profesional
    success_url = reverse_lazy('Profesional')