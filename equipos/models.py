from django.db import models
import uuid


class Equipo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)    
    fecha_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='equipos/images/', null=True, blank=True)


    def __str__(self):
        return self.nombre