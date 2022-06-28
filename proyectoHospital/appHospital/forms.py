from django import forms
from .models import *

class EspecialidadAgregar(forms.Form):
    nombre = forms.CharField(max_length=20)

class ProfesionalEditar(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    email = forms.EmailField()