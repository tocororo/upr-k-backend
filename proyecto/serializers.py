from rest_framework import serializers
from proyecto.models import proyecto


class ProyectoSerializers(serializers.ModelSerializer):
    class Meta:
        model = proyecto
        fields = "__all__"
