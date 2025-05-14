from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Sancion
from .serializers import SancionSerializer

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
