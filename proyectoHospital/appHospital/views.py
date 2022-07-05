from email import message
from msilib.schema import ListView
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Blog, Especialidad, Hospital, Profesional
from .forms import EspecialidadAgregar, ProfesionalEditar, UserEditForm, UserRegistrationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cuentas(request):
    return render(request, 'cuentas.html')

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

def especialidadLeer(request):
    especialidades = Especialidad.objects.all()
    contexto = {'especialidades':especialidades}
    return render(request, 'especialidad.html', contexto)

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

class HospitalDetalle(DetailView):
    model = Hospital
    success_url = reverse_lazy('Hospital')
    fields = ['nombre', 'zona', 'public']

class EspecialidadDetalle(DetailView):
    model = Especialidad
    success_url = reverse_lazy('Especialidad')
    fields = ['nombre']

class ProfesionalCrear(LoginRequiredMixin, CreateView):
    model = Profesional
    success_url = reverse_lazy('Profesional')
    fields = ['nombre', 'apellido', 'edad', 'email', 'matrícula', 'especialidad', 'hospital']

class ProfesionalEdicion(LoginRequiredMixin, UpdateView):
    model = Profesional
    success_url = reverse_lazy('Profesional')
    fields = ['nombre', 'apellido', 'edad', 'email', 'matrícula', 'especialidad', 'hospital']

class ProfesionalEliminar(LoginRequiredMixin, DeleteView):
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

def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, 'index.html', {'msg': 'Datos actualizados'})
    else:
        formulario  = UserEditForm(instance=usuario)
    return render(request, 'profile.html', {'formulario': formulario, 'usuario': usuario.username})

class Pagina(TemplateView):
    template_name = 'paginas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.blogobjects.all()
        return context

class PaginaDetalle(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = Blog.objects.filter(slug=self.kwargs.get('slug'))
        return context

class BlogCrear(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('paginas')
    fields = ['category', 'titulo', 'subtitulo', 'excerpt', 'contenido', 'estado', 'image']

class BlogEdicion(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy('paginas')
    fields = ['category', 'titulo', 'subtitulo', 'excerpt', 'contenido', 'estado', 'image']

class BlogEliminar(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('paginas')

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404),

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def internal_server_error(request, *args, **kwargs):
    return render(request, '500.html', status=500),
