# models.py

from django.db import models
from django.contrib.auth.models import User

class Pago(models.Model):
    TIPO_CHOICES = (
        ('cargo', 'Cargo'),
        ('abono', 'Abono'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagos')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.tipo} - {self.monto}'
