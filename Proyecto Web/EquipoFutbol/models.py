from django.db import models
from Ciudad.models import Ciudad

# Create your models here.
class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    fechafundacion = models.DateTimeField()
    cantidadtitulos = models.IntegerField()
    coloresequipacion = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE) 