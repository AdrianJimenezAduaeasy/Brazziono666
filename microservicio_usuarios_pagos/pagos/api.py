from rest_framework import viewsets, permissions
from .models import Pago
from .serializers import PagoSerializer
from .permissions import PagoPermission
from rest_framework.exceptions import PermissionDenied


class PagoViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    permission_classes = [permissions.IsAuthenticated, PagoPermission]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Pago.objects.all().order_by('-fecha')
        return Pago.objects.filter(usuario=user).order_by('-fecha')

    def perform_create(self, serializer):
        # Solo usuarios normales pueden crear
        if self.request.user.is_staff:
            raise PermissionDenied("El staff no puede crear pagos.")
        serializer.save(usuario=self.request.user)
