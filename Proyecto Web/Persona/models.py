from django.db import models
from Ciudad.models import Ciudad
from Tipodocumento.models import Tipodocumento

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    idtipodocumento = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE)
    documento = models.IntegerField()
    lugarresidencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE) #Asumí que esto era la llave foranea de ciudad?
    fechanacimiento = models.DateTimeField()
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)