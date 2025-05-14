from rest_framework.viewsets import ModelViewSet
from equipos.models import Equipo
from equipos.apiequipos.serializers import EquipoSerializer



class EquipoViewSet(ModelViewSet):
    serializer_class = EquipoSerializer
    queryset = Equipo.objects.all()