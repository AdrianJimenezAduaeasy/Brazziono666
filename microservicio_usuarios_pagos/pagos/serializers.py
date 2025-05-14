# serializers.py

from rest_framework import serializers
from .models import Pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id', 'tipo', 'monto', 'concepto', 'fecha']
        read_only_fields = ['fecha']
    
    
