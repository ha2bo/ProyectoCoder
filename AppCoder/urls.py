
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agregacurso/<nombre>/<camada>', curso),
    path('listcurso/', lista_curso),
]
