import imp
from django import forms




class EquipoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    pais= forms.CharField(max_length=50)

class EntrenaForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    experiencia= forms.CharField(max_length=30)
    nacionalidad= forms.CharField(max_length=30)

class JugaForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    posicion= forms.CharField(max_length=30)
    numero= forms.IntegerField()

#class CursoForm(forms.Form):
    #nombre = forms.CharField(max_length=50)
    #comision = forms.IntegerField()

#class ProfeForm(forms.Form):
    #nombre= forms.CharField(max_length=50)
    #apellido= forms.CharField(max_length=50)
    #email= forms.EmailField()
    #profesion= forms.CharField(max_length=50)