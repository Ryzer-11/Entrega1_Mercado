from django.urls import path

from .views import *

urlpatterns = [
   
    
    #path('curso/', curso),
    path('equiposfutbol/', equiposfutbol, name='equiposfutbol'),
    path('entrenadores/', entrenadores, name='entrenadores'),
    path('jugadores/', jugadores, name='jugadores'),
    #path('cursos/', cursos, name='cursos'),
    path('', inicio, name='inicio'), #esta era nuestra primer view
    path('entrenadorFormulario/', entrenadorFormulario, name='entrenadorFormulario'),
    path('equipoFormulario/', equipoFormulario, name='equipoFormulario'),
    path('jugadorFormulario/', jugadorFormulario, name='jugadorFormulario'),
    path('busquedaEntrenador/', busquedaEntrenador, name='busquedaEntrenador'),
    path('busquedaEquipo/', busquedaEquipo, name='busquedaEquipo'),
    path('busquedaJugador/', busquedaJugador, name='busquedaJugador'),
    path('buscar/', buscar, name='buscar'),
]