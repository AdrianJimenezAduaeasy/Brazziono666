from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication  # o JWTAuthentication
from juegos_core.permissions import EsAdminStaff
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import Juego
from .serializers import JuegoSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff])
@csrf_exempt
@api_view(['POST'])
def crear_juego_servicio(request):
    if not request.data:
        return Response({
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': 'Los datos para crear el juego no pueden estar vacíos.',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)

    serializer = JuegoSerializer(data=request.data)
    if serializer.is_valid():
        try:
            juego_guardado = serializer.save()
            datos_respuesta = JuegoSerializer(juego_guardado).data
            return Response({
                'status_code': status.HTTP_201_CREATED,
                'message': 'Juego creado exitosamente.',
                'data': datos_respuesta
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'Error interno del servidor al guardar el juego: {str(e)}',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': 'Error en los datos proporcionados para el juego.',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
@api_view(['GET'])
def listar_juegos_servicio(request):
    juegos = Juego.objects.all()
    serializer = JuegoSerializer(juegos, many=True)
    return Response({
        'status_code': status.HTTP_200_OK,
        'message': 'Lista de juegos obtenida exitosamente.',
        'data': serializer.data
    }, status=status.HTTP_200_OK)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff])
@csrf_exempt
@api_view(['PUT'])
def actualizar_juego_servicio(request, id_juego):
    try:
        juego = Juego.objects.get(id=id_juego)
    except Juego.DoesNotExist:
        return Response({
            'status_code': status.HTTP_404_NOT_FOUND,
            'message': 'Juego no encontrado.',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = JuegoSerializer(juego, data=request.data)
    if serializer.is_valid():
        try:
            juego_actualizado = serializer.save()
            return Response({
                'status_code': status.HTTP_200_OK,
                'message': 'Juego actualizado exitosamente.',
                'data': JuegoSerializer(juego_actualizado).data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'Error interno al actualizar el juego: {str(e)}',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': 'Datos inválidos para actualizar el juego.',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
