from django.urls import path
from . import views

urlpatterns = [
    path('',views.bienvenida),
    path('mostrar_mensajes',views.ver_mensajes)
]