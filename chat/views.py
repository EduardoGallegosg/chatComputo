from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Mensajes
# Create your views here.

def bienvenida(request):
    return HttpResponse("<h1>Luis Eduardo Gallegos Garcia</h1><br/><a href='mostrar_mensajes'><h2>Ver mensajes</h2></a>")

def ver_mensajes(request):
    mensaje = Mensajes.objects.all()
    return render(request, 'mensajes.html', {'mensajes': mensaje})