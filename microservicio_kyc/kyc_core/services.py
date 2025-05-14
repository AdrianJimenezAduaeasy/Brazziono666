from .serializers import KycSerializer, BaseResponseSerializer
from .models import VerificacionKYC
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@csrf_exempt
@api_view(['POST'])
def crear_kyc(request):
    if not request.data:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Los datos de KYC no pueden estar vacíos',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)

    if VerificacionKYC.objects.filter(usuario=request.data.get('usuario')).exists():
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Ya existe un KYC para este usuario',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    serializer = KycSerializer(data=request.data)
    if serializer.is_valid():
        kyc = serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'KYC creado exitosamente',
            'data': KycSerializer(kyc).data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Error en los datos de KYC',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

@csrf_exempt
@api_view(['GET'])
def obtener_kyc(request, kyc_id):
    if not kyc_id:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'El ID de KYC no puede ser nulo',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        kyc = VerificacionKYC.objects.get(id=kyc_id)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'KYC obtenido exitosamente',
            'data': KycSerializer(kyc).data
        })
    except VerificacionKYC.DoesNotExist:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'KYC no encontrado',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)
    
    
@csrf_exempt
@api_view(['GET'])
def listar_kyc(request):
    kyc = VerificacionKYC.objects.all()
    serializer = KycSerializer(kyc, many=True)
    return Response({
        'status': status.HTTP_200_OK,
        'message': 'Lista de KYC obtenida exitosamente',
        'data': serializer.data
    }, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['PUT'])
def actualizar_kyc(request, kyc_id):
    if not kyc_id:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'El ID de KYC no puede ser nulo',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        kyc = VerificacionKYC.objects.get(id=kyc_id)
    except VerificacionKYC.DoesNotExist:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'KYC no encontrado',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = KycSerializer(kyc, data=request.data)
    if serializer.is_valid():
        kyc = serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'KYC actualizado exitosamente',
            'data': KycSerializer(kyc).data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Error en los datos de KYC',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)