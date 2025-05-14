from django.db import models

class Apuesta(models.Model):
    id_usuario = models.IntegerField(db_column='id_usuario')
    id_juego = models.IntegerField(db_column='id_juego')
    monto_apuesta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_apuesta = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)

    class Meta:
        db_table = 'apuesta'

    def __str__(self):
        return f"Apuesta #{self.id} - Usuario {self.id_usuario}"
