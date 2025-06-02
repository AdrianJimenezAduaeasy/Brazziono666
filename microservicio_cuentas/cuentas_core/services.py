from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Cuenta, ReporteCuenta
from .serializers import CuentaSerializer, ReporteCuentaSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication  # o JWTAuthentication
from cuentas_core.permissions import EsAdminStaff
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
@api_view(['POST'])
def crear_cuenta(request): 
    if not request.data:  
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Los datos de la cuenta no pueden estar vacíos',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if Cuenta.objects.filter(usuario=request.data.get('usuario')).exists():
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Ya existe una cuenta para este usuario',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = CuentaSerializer(data=request.data)
    if serializer.is_valid():
        cuenta = serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'Cuenta creada exitosamente',
            'data': CuentaSerializer(cuenta).data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Error en los datos de la cuenta',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff]) 
@api_view(['GET'])
def obtener_cuenta(request, cuenta_id):
    if not  cuenta_id:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'El ID de usuario no puede ser nulo',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        cuenta = Cuenta.objects.get(usuario= cuenta_id)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Cuenta obtenida exitosamente',
            'data': CuentaSerializer(cuenta).data
        })
    except Cuenta.DoesNotExist:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'Cuenta no encontrada',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff])
@api_view(['GET'])
def obtener_cuentas(request):  
    cuentas = Cuenta.objects.all()
    if cuentas.exists():
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Cuentas obtenidas exitosamente',
            'data': CuentaSerializer(cuentas, many=True).data
        })
    else:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'No se encontraron cuentas',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff]) 
@api_view(['PUT'])
def actualizar_cuenta(request, cuenta_id): 
    if not cuenta_id or not request.data:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Datos incompletos para la actualización',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        cuenta = Cuenta.objects.get(id=cuenta_id)
        serializer = CuentaSerializer(cuenta, data=request.data, partial=True)
        
        if serializer.is_valid():
            cuenta_actualizada = serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Cuenta actualizada exitosamente',
                'data': CuentaSerializer(cuenta_actualizada).data
            })
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Error en los datos de actualización',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
    except Cuenta.DoesNotExist:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'Cuenta no encontrada',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff]) 
@api_view(['DELETE'])
def eliminar_cuenta(request, cuenta_id):  # Agregado request como primer parámetro
    if not cuenta_id:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'El ID de cuenta no puede ser nulo',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        cuenta = Cuenta.objects.get(id=cuenta_id)
        cuenta.delete()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Cuenta eliminada exitosamente',
            'data': None
        })
    except Cuenta.DoesNotExist:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'Cuenta no encontrada',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)
    
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
@api_view(['PUT'])
def recargar_cuenta(request, cuenta_id):
    if not cuenta_id or not request.data:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Datos incompletos para la recarga',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        cuenta = Cuenta.objects.get(id=cuenta_id)
        cantidad = request.data.get('cantidad')
        
        if cantidad <= 0:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'La cantidad a recargar debe ser mayor que cero',
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        cuenta.saldo += cantidad
        cuenta.save()
        
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Cuenta recargada exitosamente',
            'data': CuentaSerializer(cuenta).data
        })
    except Cuenta.DoesNotExist:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'Cuenta no encontrada',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff]) 
@api_view(['POST']) 
def crear_reporte_cuenta(request):
    if not request.data:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Los datos del reporte no pueden estar vacíos',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ReporteCuentaSerializer(data=request.data)
    if serializer.is_valid():
        reporte = serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'Reporte creado exitosamente',
            'data': ReporteCuentaSerializer(reporte).data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Error en los datos del reporte',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff]) 
@api_view(['GET'])
def obtener_reportes_cuenta(request, cuenta_id):
    if not cuenta_id:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'El ID de cuenta no puede ser nulo',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    reportes = ReporteCuenta.objects.filter(cuenta=cuenta_id)
    if reportes.exists():
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Reportes obtenidos exitosamente',
            'data': ReporteCuentaSerializer(reportes, many=True).data
        })
    else:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'No se encontraron reportes para esta cuenta',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)
    
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, EsAdminStaff]) 
@api_view(['GET'])
def consultar_reportes(request):
    reportes = ReporteCuenta.objects.all()
    if reportes.exists():
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Reportes obtenidos exitosamente',
            'data': ReporteCuentaSerializer(reportes, many=True).data
        })
    else:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'No se encontraron reportes',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)