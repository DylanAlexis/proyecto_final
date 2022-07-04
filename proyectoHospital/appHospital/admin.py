from calendar import c
from django.contrib import admin
from .models import Blog, Categoria, Comentarios, Hospital, Profesional, Especialidad
from . import models

@admin.register(models.Blog)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id', 'estado', 'slug','autor')
    prepopulated_fields = {'slug': ('titulo',), }

@admin.register(models.Comentarios)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'nombre', 'email', 'publicado','estado')
    list_filter = ('estado', 'publicado')
    search_fields = ('nombre', 'email', 'contenido')

admin.site.register(Hospital)
admin.site.register(Profesional)
admin.site.register(Especialidad)
admin.site.register(Categoria)