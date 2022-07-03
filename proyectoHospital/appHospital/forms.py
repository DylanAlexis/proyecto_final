from distutils.command.build_scripts import first_line_re
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EspecialidadAgregar(forms.Form):
    nombre = forms.CharField(max_length=20)

class ProfesionalEditar(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    email = forms.EmailField()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput())  

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label='Cambiar nombre', required=False)
    last_name = forms.CharField(label='Cambiar apellido', required=False)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(), required=False)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(), required=False)  

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}