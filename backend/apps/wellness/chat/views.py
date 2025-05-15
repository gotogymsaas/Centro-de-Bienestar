from django.shortcuts import render
from django.http import JsonResponse
import requests

def chat_view(request):
    """
    Vista que muestra la interfaz del chat.
    """
    return render(request, 'chat/chat.html')

def ai_response(request):
    """
    Endpoint para obtener la respuesta del agente de IA.
    Se espera recibir un POST con el mensaje del usuario.
    """
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        # Llama a la API del agente de IA (ajusta la URL según tu configuración)
        try:
            response = requests.post(
                'http://api.tu-agente-ai.com/get_response',  # Reemplaza con la URL real
                data={'input': user_input}
            )
            data = response.json()
            return JsonResponse({'response': data.get('response', 'No se obtuvo respuesta')})
        except Exception as e:
            return JsonResponse({'response': 'Error al procesar la solicitud: ' + str(e)})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

