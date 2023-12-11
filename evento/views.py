from django.shortcuts import render
from rest_framework import viewsets
from .models import evento
from .serializers import EventoSerializer

# Create your views here.
class EventoViewSet(viewsets.ModelViewSet):
    queryset = evento.objects.all()
    serializer_class = EventoSerializer