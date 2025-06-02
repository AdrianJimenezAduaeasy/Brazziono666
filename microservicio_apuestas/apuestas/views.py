from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Apuesta
from .forms import ApuestaForm

def home(request):
    return HttpResponse("Bienvenido a la aplicación de apuestas.")

@csrf_exempt
def realizar_apuesta(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = ApuestaForm(data)
        if form.is_valid():
            apuesta = form.save()
            return JsonResponse({'mensaje': 'Apuesta realizada exitosamente', 'id': apuesta.id}, status=201)
        else:
            return JsonResponse({'errores': form.errors}, status=400)
    else:
        return JsonResponse({'mensaje': 'Usa POST para enviar una apuesta'}, status=200)

from django.http import JsonResponse
from .models import Apuesta

def listar_apuestas(request):
    apuestas = Apuesta.objects.all().order_by('-fecha_apuesta')

    lista = [
        {
            'id': a.id,
            'id_usuario': a.id_usuario,
            'id_juego': a.id_juego,
            'monto_apuesta': float(a.monto_apuesta),
            'fecha_apuesta': a.fecha_apuesta.isoformat(),
            'estado': a.estado,
        }
        for a in apuestas
    ]

    return JsonResponse(lista, safe=False)


def detalle_apuesta(request, id):
    try:
        apuesta = Apuesta.objects.get(pk=id)
        data = {
            'id': apuesta.id,
            'id_usuario': apuesta.id_usuario,
            'id_juego': apuesta.id_juego,
            'monto_apuesta': float(apuesta.monto_apuesta),
            'fecha_apuesta': apuesta.fecha_apuesta.isoformat(),
            'estado': apuesta.estado,
        }
        return JsonResponse(data, status=200)
    except Apuesta.DoesNotExist:
        return JsonResponse({'error': 'Apuesta no encontrada'}, status=404)
    

@csrf_exempt
def actualizar_estado(request, id):
    if request.method not in ('PATCH', 'POST'):
        return JsonResponse({'mensaje': 'Usa PATCH o POST para actualizar'}, status=200)

    try:
        apuesta = Apuesta.objects.get(pk=id)
    except Apuesta.DoesNotExist:
        return JsonResponse({'error': 'Apuesta no encontrada'}, status=404)

    try:
        data = json.loads(request.body)
        nuevo_estado = data.get('estado')
        if not nuevo_estado:
            return JsonResponse({'error': 'Falta campo "estado"'}, status=400)

        apuesta.estado = nuevo_estado
        apuesta.save()
        return JsonResponse({'mensaje': 'Estado actualizado', 'id': apuesta.id, 'estado': apuesta.estado}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    
    #{ "estado": "ganado" }

