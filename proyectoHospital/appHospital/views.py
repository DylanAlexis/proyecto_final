from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def hospital(request):
    hospital_list = Hospital.objects.all()
    return render(request, 'hospital.html', {'hospital' : hospital_list})

def profesional(request):
    pprofesional_list = Profesional.objects.all()
    return render(request, 'profesional.html', {'profesional' : profesional_list})

def especialidad(request):
    especialidad_list = Especialidad.objects.all()
    return render(request, 'especialidad.html', {'especialidad' : especialidad_list})
