from django.contrib import admin

#from AppCoder.views import Curso
from .models import *
# Register your models here.

#admin.site.register(Curso)
admin.site.register(EquipoFutbol)
admin.site.register(Entrenadores)
admin.site.register(Jugadores)



