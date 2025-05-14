from rest_framework import serializers
from .models import Cuenta, ReporteCuenta

class BaseResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()
    data = serializers.JSONField(required=False)

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class ReporteCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteCuenta
        fields = '__all__'