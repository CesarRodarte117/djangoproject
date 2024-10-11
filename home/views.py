# home/views.py

from django.shortcuts import render


# hacemos las vistas en funciones para 
# cargar los index y llamarlos en urls.py
def index(request):
    return render(request, 'home/index.html')

def register(request):
    return render(request, 'home/register.html')

def login(request):
    return render(request, 'home/login.html')
