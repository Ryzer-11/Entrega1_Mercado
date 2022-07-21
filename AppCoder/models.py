from django.db import models

# Create your models here.

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)

class Entrenadores(models.Model):
    nombre= models.CharField(max_length=30)
    experiencia= models.CharField(max_length=30)
    nacionalidad= models.CharField(max_length=30)

class Jugadores(models.Model):
    nombre= models.CharField(max_length=30)
    posicion= models.CharField(max_length=30)
    numero= models.IntegerField()
    #profesion= models.CharField(max_length=30)

#class Entregable(models.Model):
    #nombre= models.CharField(max_length=30)
    #fechaDeEntrega = models.DateField()  
    #entregado = models.BooleanField()

#class Familia(models.Model):
    #parentesco= models.CharField(max_length=30)
    #nombre= models.CharField(max_length=30)
    #edad= models.IntegerField()
    #fechaDeNacimiento= models.DateField()    