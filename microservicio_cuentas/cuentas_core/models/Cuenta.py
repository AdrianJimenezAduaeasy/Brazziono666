from django.db import models
from django.contrib.auth.models import User


class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('ACTIVA', 'Activa'),
            ('INACTIVA', 'Inactiva'),
        ],
        default='ACTIVA',
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.saldo}"
    
class ReporteCuenta(models.Model):
    id = models.AutoField(primary_key=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField()
    severidad = models.CharField(
        max_length=20,
        choices=[
            ('BAJA', 'Baja'),
            ('MEDIA', 'Media'),
            ('ALTA', 'Alta'),
        ],
        default='BAJA',
    )

    def __str__(self):
        return f"Reporte de {self.cuenta} - {self.fecha_reporte}"
    
