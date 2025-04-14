import random
from django.http import HttpResponse
import json

def get_first_response(request, slug=None):
    message = "Hello! I am your chatbot. I can help you with anything unless you ask me to do something illegal."
    return HttpResponse(json.dumps({"message": message}))

def bot_response(message):
    message = message.strip().lower()
    if message=='gimme image':
        random_id = random.randint(1, 1000)
        return f"https://picsum.photos/id/{random_id}/200/300"