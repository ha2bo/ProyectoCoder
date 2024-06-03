from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def curso(req, nombre, camada):

    nuevo_curso = Curso(nombre = nombre, camada = camada)
    nuevo_curso.save()

    return  HttpResponse(f'''
<p>Curso: {nuevo_curso.nombre} - Camada: {nuevo_curso.camada} creada</p>

''')

def lista_curso(req):

    lista = Curso.objects.all()

    return render(req, 'lista_cursos.html', {"lista_cursos": lista})