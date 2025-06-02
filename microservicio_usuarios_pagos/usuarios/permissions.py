from rest_framework import permissions

class CustomUserPermission(permissions.BasePermission):
    """
    Permisos personalizados:
    - Usuarios normales (`is_staff=False`) solo pueden:
        - Crear su cuenta (POST)
        - Ver su propia cuenta (GET /users/me/)
        - Editar su propia cuenta (PUT/PATCH /users/me/)
    - Usuarios staff (`is_staff=True`) pueden:
        - Ver todos los usuarios
        - Crear, editar y eliminar cualquier usuario
    """

    def has_permission(self, request, view):
        # Permitir siempre que cree (registro)
        if view.action == 'create':
            return True

        # Si es staff, permitir todo
        if request.user.is_staff:
            return True

        # Si no es staff, solo permitir ver o editar su propia cuenta
        if view.action in ['retrieve', 'update', 'partial_update']:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # Si es staff, permitir acceso al objeto
        if request.user.is_staff:
            return True

        # Si no es staff, solo puede acceder a su propio objeto
        return obj == request.user
