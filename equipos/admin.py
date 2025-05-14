from django.contrib import admin
from equipos.models import Equipo

# Register your models here.



@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'fecha_creacion', 'fecha_modificacion', 'mostrar_miembros')

    def mostrar_miembros(self, obj):
        return ", ".join([miembro.username for miembro in obj.miembros.all()])
    mostrar_miembros.short_description = 'Miembros'