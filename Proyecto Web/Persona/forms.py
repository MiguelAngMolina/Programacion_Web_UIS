from django import forms
from .models import Persona

#Crear formulario
class PersonaForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Persona

        #especificar los campos
        fields = [
            'nombre',
            'apellidos',
            'idtipodocumento',
            'documento',
            'lugarresidencia',
            'fechanacimiento',
            'email',
            'telefono',
            'usuario',
            'password'
        ]