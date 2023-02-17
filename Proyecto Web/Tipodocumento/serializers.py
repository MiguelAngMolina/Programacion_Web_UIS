from rest_framework import serializers
from .models import Tipodocumento

class TipoDocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipodocumento
        fields = ["id","nombre","descripcion"]