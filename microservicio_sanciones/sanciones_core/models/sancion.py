from django.db import models
from django.utils import timezone

class Sancion(models.Model):

    id_sancion = models.AutoField(primary_key=True)

    id_usuario = models.IntegerField(null=False, blank=False)

    motivo = models.TextField(null=False, blank=False)

    fecha_aplicacion = models.DateTimeField(auto_now_add=True)

    fecha_expiracion = models.DateTimeField(null=True, blank=True)

    ESTADO_ACTIVA = 'activa'
    ESTADO_EXPIRADA = 'expirada'
    ESTADO_SANCION_CHOICES = [
        (ESTADO_ACTIVA, 'Activa'),
        (ESTADO_EXPIRADA, 'Expirada'),
    ]
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_SANCION_CHOICES,
        default=ESTADO_ACTIVA
    )

    def __str__(self):
        return f"Sanción {self.id_sancion} para usuario {self.id_usuario} - {self.estado}"

    class Meta:
        db_table = 'Sanciones'
        verbose_name = 'Sanción'
        verbose_name_plural = 'Sanciones'
        ordering = ['-fecha_aplicacion']