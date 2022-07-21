#from http.client import HttpResponse
#from sqlite3 import Cursor
#from django import http
#from cgitb import text
from distutils.log import info
import email
from django.shortcuts import render, HttpResponse
from AppCoder.models import EquipoFutbol, Entrenadores, Jugadores
#from AppCoder.models import Cursos, Familia
from django.http import HttpResponse
from AppCoder.forms import EntrenaForm, EquipoForm, JugaForm

# Create your views here.


#def curso(self):

    #curso= Curso(nombre="Django", comision=31)
    #curso.save()
    #texto= f"Curso creado: {curso.nombre} {curso.comision}"
    #return HttpResponse(texto)

    
    #return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def equiposfutbol(request):

      return render(request, "AppCoder/equiposfutbol.html")

def entrenadores(request):

      return render(request, "AppCoder/entrenadores.html")


def jugadores(request):

      return render(request, "AppCoder/jugadores.html")


#def entregables(request):

      #return render(request, "AppCoder/entregables.html")

      
"""def cursoFormulario(request):

    if request.method == 'POST':

        nombre = request.POST.get("curso")
        comision = request.POST.get("comision")
        curso = Curso(nombre=nombre, comision=comision)
        curso.save()
        return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/cursoFormulario.html")"""

def entrenadorFormulario(request):

    if (request.method == "POST"):
        form= EntrenaForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            experiencia= info["experiencia"]
            nacionalidad= info["nacionalidad"]
            entrenadores= Entrenadores(nombre=nombre, experiencia=experiencia, nacionalidad=nacionalidad)
            entrenadores.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= EntrenaForm()
    return render(request, "AppCoder/entrenadorFormulario.html", {"formulario":form})    


def equipoFormulario(request):

    if (request.method == "POST"):
        form= EquipoForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            pais= info["pais"]
            #email= info["email"]
            #profesion= info["profesion"]
            equipo= EquipoFutbol(nombre=nombre, pais=pais)
            equipo.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= EquipoForm()
    return render(request, "AppCoder/equipoFormulario.html", {"formulario":form})


def jugadorFormulario(request):

    if (request.method == "POST"):
        form= JugaForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            posicion= info["posicion"]
            numero= info["numero"]
            #email= info["email"]
            #profesion= info["profesion"]
            jugadores= Jugadores(nombre=nombre, posicion=posicion, numero=numero)
            jugadores.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= JugaForm()
    return render(request, "AppCoder/jugadorFormulario.html", {"formulario":form})

     

def busquedaEntrenador(request):

    return render(request, "AppCoder/busquedaEntrenador.html")


def buscar(request):
    if request.GET["nombre"]:
        nom= request.GET["nombre"]
        entrenadores= Entrenadores.objects.filter(nombre=nom)
        return render(request, "AppCoder/resultadosEntrenador.html", {"entrenadores":entrenadores})
    else:
        return render(request, "AppCoder/busquedaEntrenador.html", {"error":"No se ingreso ningun entrenador"})


def busquedaEquipo(request):

    return render(request, "AppCoder/busquedaEquipo.html")


def buscar(request):
    if request.GET["pais"]:
        pa= request.GET["pais"]
        equiposfutbol= EquipoFutbol.objects.filter(pais=pa)
        return render(request, "AppCoder/resultadosEquipo.html", {"equiposfutbol":equiposfutbol})
    else:
        return render(request, "AppCoder/busquedaEquipo.html", {"error":"No se ingreso ningun pais"})


def busquedaJugador(request):

    return render(request, "AppCoder/busquedaJugador.html")


def buscar(request):
    if request.GET["numero"]:
        num= request.GET["numero"]
        jugadores= Jugadores.objects.filter(numero=num)
        return render(request, "AppCoder/resultadosJugador.html", {"jugadores":jugadores})
    else:
        return render(request, "AppCoder/busquedaJugador.html", {"error":"No se ingreso ningun jugador"})





#def familia(self):
    
    #familia= Familia(parentesco="Padre", nombre ="Mario Garcia Almada", edad=53, fechaDeNacimiento=16091968)
    #familia.save()
    #texto= f"Familia creado: {familia.parentesco} {familia.nombre} {familia.edad} {familia.fechaDeNacimiento}"
    #return HttpResponse(texto)