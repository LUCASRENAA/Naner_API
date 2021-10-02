from rest_framework import viewsets, generics
from rest_framework import status
from naner.models import  Milhar_Jogo, Jogo
from naner.serializer import  NotaSerializer, JogoSerializer
from rest_framework.response import Response





class NotaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Milhar_Jogo.objects.all()
    serializer_class = NotaSerializer
    http_method_names = ['get', 'post', 'put', 'path']

class JogoViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    http_method_names = ['get', 'post', 'put', 'path']

