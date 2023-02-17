from django.db import models

# Modelo de la ciudad.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)