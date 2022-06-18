from django.shortcuts import render
from .

# Create your views here.

def home(request):
    return render(request, 'base.html')

def register(request):
    return render(request, 'register.html')    