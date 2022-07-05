from email.policy import default
from importlib.metadata import requires
import os
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone

class Hospital(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4(), primary_key=True)
    nombre = models.CharField(max_length=50)
    zona = models.CharField(max_length=30)
    public = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.public == True:
            return self.nombre+" | "+self.zona+" | Público"
        else:
            return self.nombre+" | "+self.zona+" | Privado"

class Especialidad(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4(), primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre

class Profesional(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4(), primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    matrícula = models.CharField(max_length=15)
    edad = models.IntegerField()
    email = models.EmailField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido+" | "+str(self.especialidad)

class Categoria(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Blog(models.Model):

    class BlogObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(estado='publicado')

    opciones = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    category = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    contenido = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="publicado", null=False, unique=True)
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    estado = models.CharField(max_length=10, choices=opciones, default='borrador')
    objects = models.Manager()
    blogobjects = BlogObjects()
    image = models.ImageField(upload_to='img')

    class Meta:
        ordering = ('publicado',)

    def __str__(self) -> str:
        return self.titulo

class Comentarios(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    contenido = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ('publicado',)

        def __str__(self):
            return f'Comentario de {self.nombre}'