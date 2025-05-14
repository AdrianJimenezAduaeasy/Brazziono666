from rest_framework import serializers
from .models import Juego

class JuegoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juego
        fields = ['id', 'nombre_juego', 'descripcion', 'estado']
        read_only_fields = ['id']
