from django.contrib import admin
from partidos.models import Partido



@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora', 'lugar', 'equipo_local', 'equipo_visitante')