from django.db import models

# Create your models here.
class evento(models.Model):
    nombre_evento = models.CharField(max_length=250)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    descripcion = models.CharField(max_length=400)
    tipo_evento = models.CharField(max_length=250)
    lugar_evento = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre_evento