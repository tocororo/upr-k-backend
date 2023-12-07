from django.db import models


# Create your models here.
class proyecto(models.Model):
    nombre_proyecto=models.CharField(max_length=250)
    descripcion=models.CharField(max_length=250)
    lider_proyecto=models.CharField(max_length=250)
    objetivos=models.CharField(max_length=250)
    linea_de_investigacion=models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre_proyecto