from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(resquest):
    return render(resquest, 'recipes/pages/home.html')
