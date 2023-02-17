from django import forms
from .models import EquipoFutbol

#Crear formulario Tipodocumentio
class EquipoFutbolForm(forms.ModelForm):
    class Meta:
        model = EquipoFutbol
        fields = [
            'nombre',
            'pais',
            'estadio',
            'fechafundacion',
            'cantidadtitulos',
            'coloresequipacion',
            'ciudad'
        ]