from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')  # Asegúrate de tener este archivo HTML en la carpeta de templates
