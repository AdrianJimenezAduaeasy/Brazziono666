from rest_framework import permissions

class PagoPermission(permissions.BasePermission):
    """
    - Usuarios normales: pueden crear y ver solo sus pagos.
    - Staff: puede ver, editar y eliminar cualquier pago, pero no puede crear.
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            # Staff puede hacer todo excepto crear pagos
            return view.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']
        else:
            # Usuario normal puede listar, ver y crear sus propios pagos
            return view.action in ['list', 'retrieve', 'create']

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.usuario == request.user
