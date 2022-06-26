from django.db import models
import uuid

class Hospital(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4(), primary_key=True)
    nombre = models.CharField(max_length=50)
    zona = models.CharField(max_length=30)
    public = models.BooleanField(default=False)

class Especialidad(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4(), primary_key=True)
    nombre = models.CharField(max_length=20)

class Profesional(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4(), primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    matrícula = models.CharField(max_length=15)
    edad = models.IntegerField(max_length=3)
    email = models.EmailField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)