from django.db import models

class Juego(models.Model):
    ESTADO_ACTIVO = 'activo'
    ESTADO_INACTIVO = 'inactivo'
    ESTADO_CHOICES = [
        (ESTADO_ACTIVO, 'Activo'),      # El primer valor se guarda en la BD, el segundo es legible por humanos
        (ESTADO_INACTIVO, 'Inactivo'),
    ]

    nombre_juego = models.CharField(max_length=100, null=False, blank=False) # VARCHAR(100) NOT NULL
    # En Django, null=False y blank=False son los valores por defecto para CharField,
    # así que `null=False, blank=False` es explícito pero no estrictamente necesario aquí.

    descripcion = models.TextField(null=True, blank=True) # TEXT, permite valores nulos y vacíos

    estado = models.CharField(
        max_length=10,  # Longitud suficiente para 'activo' o 'inactivo'
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO # DEFAULT 'activo'
    )

    # Opcional: Django puede añadir campos de fecha de creación/actualización automáticamente
    # fecha_creacion = models.DateTimeField(auto_now_add=True)
    # fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Esto define cómo se representará un objeto Juego como string
        # (por ejemplo, en el panel de administración de Django).
        return self.nombre_juego

    class Meta:
        # Esto es opcional, pero es buena práctica.
        db_table = 'Juegos'  # Asegura que Django use 'Juegos' como nombre de tabla en la BD.
                             # Si no se especifica, Django usaría 'juegos_core_juego'.
        verbose_name = 'Juego' # Nombre legible para el modelo en singular.
        verbose_name_plural = 'Juegos' # Nombre legible para el modelo en plural.