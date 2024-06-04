from django.db import models

# Create your models here.
#los modelos son para la base de datos, es como crear la tablas


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(null= True)


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(null= True)
    profesion = models.CharField(max_length= 40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()