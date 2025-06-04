from django.http import HttpRequest

def home(request):
    return HttpRequest("Welcome to my django application.")