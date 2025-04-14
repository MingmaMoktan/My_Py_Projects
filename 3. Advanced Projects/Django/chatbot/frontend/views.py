from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def frontend(request, slug=None):
    return render(request, 'frontend/template_chatbot.html')