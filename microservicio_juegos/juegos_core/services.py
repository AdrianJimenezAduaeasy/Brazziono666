from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Juego
from .serializers import JuegoSerializer

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