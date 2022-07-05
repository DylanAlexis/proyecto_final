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
from django.conf import settings
from django.conf.urls.static import static
from appHospital.views import (
    Pagina, PaginaDetalle, HospitalDetalle, EspecialidadDetalle, ProfesionalCrear, ProfesionalDetalle, ProfesionalEdicion,
    ProfesionalEliminar, ProfesionalList, BlogCrear, BlogEdicion, BlogEliminar, editarPerfil, especialidadLeer, especialidadAgregar,
    hospitalLeer, index, about, login_request, profesionalBuscar, profesionalBuscarResultado, profesionalEditar,
    profesionalEliminar, profesionalLeer, register_request, cuentas
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

    path('cuentas', cuentas, name='cuentas'),
    path('cuentas/login/', login_request, name='login'),
    path('cuentas/register/', register_request, name='register'),
    path('cuentas/logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('cuentas/profile/', editarPerfil, name='EditarPerfil'),

    path('paginas/', Pagina.as_view(), name='paginas'),
    path('paginas/<slug>/', PaginaDetalle.as_view(), name='pagina_detalle'),

    path('/paginas/nuevo/', BlogCrear.as_view(), name='pagina_crear'),
    path('/paginas/edicion/<slug>', BlogEdicion.as_view(), name='pagina_edicion'),
    path('/paginas/borrar/<slug>', BlogEliminar.as_view(), name='pagina_eliminar'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "appHospital.views.page_not_found_view"
handler500 = "appHospital.views.internal_server_error"