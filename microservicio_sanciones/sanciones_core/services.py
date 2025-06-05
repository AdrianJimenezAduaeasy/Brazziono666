from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from sanciones_core.permissions import EsAdminStaff
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response

from .models import Sancion
from .serializers import SancionSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff])
@csrf_exempt
@api_view(['POST'])
def aplicar_sancion_servicio(request):
    """
    Endpoint para aplicar una nueva Sanción a un usuario.
    Espera datos en el cuerpo de la solicitud POST.
    """
    if not request.data:
        return Response({
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': 'Los datos para aplicar la sanción no pueden estar vacíos.',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)

    serializer = SancionSerializer(data=request.data)
    if serializer.is_valid():
        try:
            sancion_guardada = serializer.save()
            datos_respuesta = SancionSerializer(sancion_guardada).data
            return Response({
                'status_code': status.HTTP_201_CREATED,
                'message': 'Sanción aplicada exitosamente.',
                'data': datos_respuesta
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'Error interno del servidor al aplicar la sanción: {str(e)}',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': 'Error en los datos proporcionados para la sanción.',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
# Si quieres que listar_sanciones_servicio sea accesible sin token para usuarios normales,
# deberías usar @permission_classes([AllowAny]) aquí, como mencionamos antes.
# Tal como está, con IsAuthenticated, requiere un token para listar.
@csrf_exempt
@api_view(['GET'])
def listar_sanciones_servicio(request):
    """
    Endpoint para listar todas las sanciones.
    """
    try:
        sanciones = Sancion.objects.all()
        serializer = SancionSerializer(sanciones, many=True)
        return Response({
            'status_code': status.HTTP_200_OK,
            'message': 'Listado de sanciones obtenido exitosamente.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': f'Error interno al obtener las sanciones: {str(e)}',
            'data': None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --- ¡ELIMINA ESTA LÍNEA! ---

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff])
@csrf_exempt
@api_view(['PUT'])
def actualizar_sancion_servicio(request, sancion_id):
    """
    Endpoint para actualizar una sanción existente por su ID.
    """
    try:
        sancion = Sancion.objects.get(id_sancion=sancion_id) # Esta línea ya estaba corregida
    except Sancion.DoesNotExist:
        return Response({
            'status_code': status.HTTP_404_NOT_FOUND,
            'message': 'La sanción no existe.',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = SancionSerializer(sancion, data=request.data, partial=True)
    if serializer.is_valid():
        try:
            sancion_actualizada = serializer.save()
            return Response({
                'status_code': status.HTTP_200_OK,
                'message': 'Sanción actualizada correctamente.',
                'data': SancionSerializer(sancion_actualizada).data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'Error interno al actualizar la sanción: {str(e)}',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': 'Datos inválidos para actualizar la sanción.',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)