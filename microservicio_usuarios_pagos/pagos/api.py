# views.py

from rest_framework import viewsets, permissions
from .models import Pago
from .serializers import PagoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pago.objects.filter(usuario=self.request.user).order_by('-fecha')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
