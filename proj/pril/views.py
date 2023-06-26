from django.shortcuts import render
from .models import MessageFront
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


def show_all_message(request):
    messages = MessageFront.objects.all()
    return render(request, 'pril/all_message.html', {'messages': messages})


@csrf_exempt
def save_json(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        MessageFront.objects.create(
            user=data.get('user'),
            date=data.get('date'),
            screen=data.get('screen'),
            event=data.get('event')
        )
        return JsonResponse({'message': 'Success'})
    return JsonResponse({'message': 'Invalid request method'})
