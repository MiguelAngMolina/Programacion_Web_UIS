from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ["id","nombre","apellidos","idtipodocumento","documento","lugarresidencia","fechanacimiento", "email", "telefono", "usuario","password"]