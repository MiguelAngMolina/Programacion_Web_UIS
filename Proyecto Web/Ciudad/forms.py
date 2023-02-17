from django import forms
from .models import Ciudad

#Crear formulario Tipodocumentio
class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad

        fields = [
            'nombre',
            'descripcion'
        ]