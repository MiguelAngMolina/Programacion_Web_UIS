from rest_framework import serializers
from .models import EquipoFutbol

class EquipoFutbolSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipoFutbol
        fields = ["id","nombre","pais","estadio", "fechafundacion", "cantidadtitulos", "coloresequipacion", "ciudad"]