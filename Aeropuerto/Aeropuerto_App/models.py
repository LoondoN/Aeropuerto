from asyncio import AbstractServer
from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False,null=True)
    token = models.CharField(max_length=100, default='', null=True, blank=True)

class Avion(models.Model):
    codigo_avion = models.CharField(max_length=20,unique=True)
    tipo_avion = models.CharField(max_length=20)
    ciudad_base =models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)
    def __str__(self):
        return self.codigo_avion

class Piloto(models.Model):
    codigo_piloto = models.CharField(max_length=20,unique=True)
    nombre_pilo = models.CharField(max_length=20)
    horas_vuelo_piloto = models.IntegerField()
    def __str__(self):
        return self.nombre_pilo

class Tripulacion(models.Model):
    codigo_Tripulante = models.CharField(max_length=20,unique=True)
    nombre_tripulante = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre_tripulante

class Vuelo(models.Model):
    numero_vuelo = models.CharField(max_length=20,unique=True)
    avion = models.ForeignKey(Avion,on_delete=models.PROTECT)
    piloto = models.ForeignKey(Piloto,on_delete=models.PROTECT)
    origen = models.CharField(max_length=20)
    destino = models.CharField(max_length=20)
    def __str__(self):
        return self.numero_vuelo

class Itinerario(models.Model):
    codigo_Tabla =models.CharField(max_length=20,unique=True)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.PROTECT)
    tripulacion = models.ForeignKey(Tripulacion, on_delete=models.PROTECT)