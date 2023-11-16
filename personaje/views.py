from rest_framework import viewsets
from .models import personaje
from .serializers import PersonajeSerializers


class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = personaje.objects.all()
    serializer_class = PersonajeSerializers
