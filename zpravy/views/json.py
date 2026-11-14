


import json
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from zpravy.models import ChatMessage


@login_required
def odeslat_zpravu_api(request):
  """API endpoint pro odeslání zprávy přes JavaScript bez reloadu"""
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      text_zpravy = data.get('message')
      prijemce_id = data.get('receiver_id')

      if not text_zpravy:
        return JsonResponse(
            {'status': 'error', 'message': 'Zpráva nemůže být prázdná.'},
            status=400,
        )

      prijemce = get_object_or_404(User, id=prijemce_id)

      # Vytvoření zprávy v databázi
      zprava = ChatMessage.objects.create(
          sender=request.user, receiver=prijemce, message=text_zpravy
      )

      return JsonResponse({
          'status': 'success',
          'message': zprava.message,
          'time': zprava.timestamp.strftime('%H:%M'),
      })
    except Exception as e:
      return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

  return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)