from django.db import models
from django.contrib.auth.models import User


class VerificacionKYC(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    documento_identidad = models.CharField(max_length=255)
    documento_identidad_direccion = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('PENDIENTE', 'Pendiente'),
            ('APROBADO', 'Aprobado'),
            ('RECHAZADO', 'Rechazado'),
        ],
        default='PENDIENTE',
    )
    