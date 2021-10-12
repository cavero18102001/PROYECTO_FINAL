from django.db import models
from datetime import datetime

# Create your models here.
class Consulta(models.Model):
    idConsulta = models.CharField(max_length=100,primary_key=True)
    dia = models.DateTimeField(default=datetime.now, blank=True)
    estado = models.CharField(max_length=1,default="A")


class Mensaje(models.Model):
    idMensaje= models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=500)
    hora = models.DateTimeField(default=datetime.now, blank=True)
    usuario = models.CharField(max_length=10)
    estado = models.CharField(max_length=1,default="A")
    idConsulta = models.CharField(max_length=100)

class Persona(models.Model):
    idPersona =models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    hora = models.DateTimeField(default=datetime.now, blank=True)
    estado = models.CharField(max_length=1,default="A")