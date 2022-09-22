from django.shortcuts import render
from django.http import HttpResponse

from app1.models import Vuelo, Personal, Pasajero

from app1.forms import FormuVuelo, FormuPersonal, FormuPasajero

# Create your views here.


def inicio(request):
    return render(request,'app1/inicio.html')





#vuelos

def vuelo(request):
    return render(request,'app1/vuelo.html')


def formulariovuelo(request):
    if request.method=="POST":#si yo le doy al boton GO
        formulariovuelo = FormuVuelo(request.POST)
        if formulariovuelo.is_valid():
            info = formulariovuelo.cleaned_data
            vuelof = Vuelo(id_vuelo = info["id_vuelo"], salida = info["salida"], destino = info["destino"], fecha = info["fecha"], hora_de_salida = info["hora_de_salida"])#lee la informacion de las cajas de texto
            vuelof.save()#guardar en la base de datos
            return render(request,"app1/inicio.html")#despues de enviar salta esta pagina
    else:
        formulariovuelo = FormuVuelo()
    return render(request,"app1/FVuelo.html",{"formulario1":formulariovuelo})#cuando entro a la pagina web por primera vez sale este return


def busquedaVuelos(request):
    return render(request,"app1/busquedaVuelos.html")


def buscar(request):
    if request.GET["salida"]:
        busqueda = request.GET["salida"]
        vuelos = Vuelo.objects.filter(salida=busqueda)#puede ir tambien camada__icontains = busqueda
        return render(request,"app1/vuelo.html",{"vuelos":vuelos, "busqueda":busqueda})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando el vuelo que sale de: {busqueda}")






#personal

def personal(request):
    return render(request,'app1/personal.html')


def formulariopersonal(request):
    if request.method=="POST":
        formulariopersonal = FormuPersonal(request.POST)
        if formulariopersonal.is_valid():
            info = formulariopersonal.cleaned_data
            personalf = Personal(nombre = info["nombre"], apellido = info["apellido"], profesion = info["profesion"],  id_vuelo = info["id_vuelo"])
            personalf.save()
            return render(request,"app1/inicio.html")
    else:
        formulariopersonal = FormuPersonal()
    return render(request,"app1/FPersonal.html",{"formulario2":formulariopersonal})


def busquedaPersonal(request):
    return render(request,"app1/busquedaPersonal.html")


def buscar_per(request):
    if request.GET["profesion"]:
        busqueda_per = request.GET["profesion"]
        personas = Personal.objects.filter(profesion = busqueda_per)
        return render(request,"app1/personal.html",{"personas":personas, "busqueda_per":busqueda_per})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando la profesión: {busqueda_per}")








#pasajero

def pasajero(request):
    return render(request,'app1/pasajero.html')


def formulariopasajero(request):
    if request.method=="POST":
        formulariopasajero = FormuPasajero(request.POST)
        if formulariopasajero.is_valid():
            info = formulariopasajero.cleaned_data
            pasajerof = Pasajero(nombre = info["nombre"], apellido = info["apellido"], documento = info["documento"], id_vuelo = info["id_vuelo"])
            pasajerof.save()
            return render(request,"app1/inicio.html")
    else:
        formulariopasajero = FormuPasajero()
    return render(request,"app1/FPasajero.html",{"formulario3":formulariopasajero})


def busquedaPasajero(request):
    return render(request,"app1/busquedaPasajero.html")


def buscar_pasa(request):
    if request.GET["id_vuelo"]:
        busqueda_pasa = request.GET["id_vuelo"]
        pasajeros = Pasajero.objects.filter(id_vuelo = busqueda_pasa)
        return render(request,"app1/pasajero.html",{"pasajeros":pasajeros, "busqueda_pasa":busqueda_pasa})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando los pasajeros del vuelo: {busqueda_pasa}")

'''



{% extends "app1/padre.html" %}



{% block titulo %}

<h1>En esta seccion agregue los datos del pasajero</h1>

{% endblock %}



{% block pie %}



<form action = "" method="POST"> {% csrf_token %}
            
    <table>
        <p>
            <h1>Ingrese datos del pasajero</h1>
                    
                {{formulario3.as_table}}
            
        </p>
    </table>

                    
    <input type="submit" value="ENVIAR">
                    
</form>
  
{% endblock %}

'''