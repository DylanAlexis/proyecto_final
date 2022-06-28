from django.db import models
import uuid

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

    def __str__(self) -> str:
        return self.nombre

class Profesional(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4(), primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    matrícula = models.CharField(max_length=15)
    edad = models.IntegerField(max_length=3)
    email = models.EmailField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido+" | "+str(self.especialidad)