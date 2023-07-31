from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(resquest):
    return render(resquest, 'recipes/home.html')

def sobre(request):
    return HttpResponse ('SOBRE 1')

def contato(request):
    return HttpResponse ('CONTATO teste')