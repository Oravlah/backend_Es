from rest_framework import serializers
from partidos.models import Partido



class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'