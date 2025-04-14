from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def backend(request, slug=None):
    return HttpResponse("<p>Hello from the backend-side</p>")

def get_chat_response(request, slug=None):
    return HttpResponse("Hello from get chat response")
# Placeholder for chat response logic
    return HttpResponse("<p>This is a placeholder for chat response</p>")