from django.db import models

# Create your models here.
#los modelos son para la base de datos, es como crear la tablas


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)