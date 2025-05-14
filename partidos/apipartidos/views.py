from rest_framework.viewsets import ModelViewSet
from partidos.models import Partido
from partidos.apipartidos.serializers import PartidoSerializer


class PartidoViewSet(ModelViewSet):
    serializer_class = PartidoSerializer
    queryset = Partido.objects.all()