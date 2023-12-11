from rest_framework import viewsets
from .models import proyecto
from .serializers import ProyectoSerializers


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = proyecto.objects.all()
    serializer_class = ProyectoSerializers
