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
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404
from appHospital.views import (
    Error404, Pagina, PaginaDetalle, HospitalDetalle, EspecialidadDetalle, ProfesionalCrear, ProfesionalDetalle, ProfesionalEdicion,
    ProfesionalEliminar, ProfesionalList, editarPerfil, especialidadLeer, especialidadAgregar,
    hospitalLeer, index, about, login_request, profesionalBuscar, profesionalBuscarResultado, profesionalEditar,
    profesionalEliminar, profesionalLeer, register_request
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('hospital/', hospitalLeer, name='Hospital'),
    path('profesional/', profesionalLeer, name='Profesional'),
    path('especialidad/', especialidadLeer, name='Especialidad'),
    path('especialidadAgregar/', especialidadAgregar, name='EspecialidadAgregar'),
    path('profesionalBuscar/', profesionalBuscar, name='ProfesionalBuscar'),
    path('profesionalBuscarResultado/', profesionalBuscarResultado, name='ProfesionalBuscarResultado'),
    path('profesionalEliminar/<apellido>', profesionalEliminar, name='ProfesionalEliminar'),
    path('profesionalEditar/<matrícula>', profesionalEditar, name='ProfesionalEditar'),

    path('profesional/list/', ProfesionalList.as_view(), name='profesional_list'),
    path('profesional/<pk>', ProfesionalDetalle.as_view(), name='profesional_detalle'),
    path('hospital/<pk>', HospitalDetalle.as_view(), name='hospital_detalle'),
    path('especialidad/<pk>', EspecialidadDetalle.as_view(), name='especialidad_detalle'),
    path('profesional/nuevo/', ProfesionalCrear.as_view(), name='profesional_crear'),
    path('profesional/edicion/<pk>', ProfesionalEdicion.as_view(), name='profesional_edicion'),
    path('profesional/borrar/<pk>', ProfesionalEliminar.as_view(), name='profesional_eliminar'),

    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='EditarPerfil'),

    path('paginas/', Pagina.as_view(), name='paginas'),
    path('paginas/<slug>/', PaginaDetalle.as_view(), name='pagina_detalle'),

]

handler404 = Error404.as_view()