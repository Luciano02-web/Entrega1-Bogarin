from django.urls import path
from app1.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('vuelo/', vuelo),
    path('personal/', personal),
    path('pasajero/', pasajero),


    path('formulario1/', formulariovuelo, name="Crear Vuelos"),
    path('formulario2/', formulariopersonal, name="Crear Personal"),
    path('formulario3/', formulariopasajero, name="Crear Pasajeros"),


    path('buscarVuelos/', busquedaVuelos, name="Buscar Vuelos"),
    path('buscarPersonal/', busquedaPersonal, name="Buscar Personal"),
    path('buscarPasajero/', busquedaPasajero, name="Buscar Pasajeros"),


    path('buscar_pasa/',buscar_pasa),
    path('buscar_per/',buscar_per),
    path('buscar/',buscar),
    ]