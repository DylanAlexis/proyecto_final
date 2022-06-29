"""proyectoHospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appHospital.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('hospital/', hospitalLeer, name='Hospital'),
    path('especialidad/', especialidad, name='Especialidad'),
    path('profesional/', profesionalLeer, name='Profesional')
    ,
    path('especialidadAgregar/', especialidadAgregar, name='EspecialidadAgregar'),
    path('profesionalBuscar/', profesionalBuscar, name='ProfesionalBuscar'),
    path('profesionalBuscarResultado/', profesionalBuscarResultado, name='ProfesionalBuscarResultado'),
    path('profesionalEliminar/<apellido>', profesionalEliminar, name='ProfesionalEliminar'),
    path('profesionalEditar/<matrícula>', profesionalEditar, name='ProfesionalEditar'),

    path('profesional/list/', ProfesionalList.as_view(), name='profesional_list'),
    path('profesional/<pk>', ProfesionalDetalle.as_view(), name='profesional_detalle'),
    path('profesional/nuevo/', ProfesionalCrear.as_view(), name='profesional_crear'),
    path('profesional/edicion/<pk>', ProfesionalEdicion.as_view(), name='profesional_edicion'),
    path('profesional/borrar/<pk>', ProfesionalEliminar.as_view(), name='profesional_eliminar'),

    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
]