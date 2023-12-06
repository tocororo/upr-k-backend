from rest_framework import serializers
from personaje.models import personaje


class PersonajeSerializers(serializers.ModelSerializer):
    class Meta:
        model = personaje
        fields = "__all__"
