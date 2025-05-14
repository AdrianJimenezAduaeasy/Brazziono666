from rest_framework import serializers
from .models import VerificacionKYC

class BaseResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()
    data = serializers.JSONField(required=False)

class KycSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacionKYC
        fields = '__all__'