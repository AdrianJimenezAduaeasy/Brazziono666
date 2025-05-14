from django import forms
from .models import Apuesta

class ApuestaForm(forms.ModelForm):
    class Meta:
        model = Apuesta
        fields = ['id_usuario', 'id_juego', 'monto_apuesta', 'estado']
