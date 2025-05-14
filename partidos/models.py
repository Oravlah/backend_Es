from django.db import models
from django.db.models import SET_NULL
import uuid
from equipos.models import Equipo
# Create your models here.





class Partido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100)
    equipo_local = models.ForeignKey(Equipo, on_delete=SET_NULL, null=True, related_name='equipo_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=SET_NULL, null=True, related_name='equipo_visitante')

