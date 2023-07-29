from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(resquest):
    return HttpResponse('Home 1')

def sobre(request):
    return HttpResponse ('SOBRE 1')

def contato(request):
    return HttpResponse ('CONTATO teste')