from django import forms
from .models import Tipodocumento

#Crear formulario Tipodocumentio
class TipodocumentoForm(forms.ModelForm):
    class Meta:
        model = Tipodocumento

        fields = [
            'nombre',
            'descripcion'
        ]