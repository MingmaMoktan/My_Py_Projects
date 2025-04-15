# backend/views.py
from django.http import HttpResponse
import json
from backend.responses import bot_response

def get_chat_response(request, slug=None):
    data = request.GET
    message = data.get("message", "")
    response = bot_response(request, message)
    return HttpResponse(json.dumps(response), content_type='application/json')

