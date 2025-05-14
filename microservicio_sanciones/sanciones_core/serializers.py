from rest_framework import serializers
from .models import Sancion

class SancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sancion
        fields = [
            'id_sancion',
            'id_usuario',
            'motivo',
            'fecha_aplicacion',
            'fecha_expiracion',
            'estado'
        ]
        read_only_fields = ['id_sancion', 'fecha_aplicacion']