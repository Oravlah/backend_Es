from rest_framework.routers import DefaultRouter
from partidos.apipartidos.views import PartidoViewSet


router_partidos = DefaultRouter()

router_partidos.register(prefix='partidos', basename='partidos', viewset=PartidoViewSet)