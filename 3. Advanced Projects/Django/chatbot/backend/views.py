from django.shortcuts import render
from django.http import HttpResponse
import json
from .responses import bot_response

# Create your views here.

def get_chat_response(request, slug=None):
    data = request.GET
    message = data.get("message")
    
    response = {
        "message": bot_response(message)
    }
    return HttpResponse(json.dumps(response))
