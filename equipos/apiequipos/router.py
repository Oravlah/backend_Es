from rest_framework.routers import DefaultRouter
from equipos.apiequipos.views import EquipoViewSet



router_equipos = DefaultRouter()

router_equipos.register(prefix='equipos', basename='equipos', viewset=EquipoViewSet)