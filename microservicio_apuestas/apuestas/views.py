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

