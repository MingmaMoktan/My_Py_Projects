from django.shortcuts import render

# Create your views here.
def frontend(request, slug=None):
    return render(request, 'frontend/template_chatbot.html')
