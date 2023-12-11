from rest_framework import serializers
from .models import evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = evento
        fields = '__all__'