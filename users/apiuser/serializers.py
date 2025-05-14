from rest_framework  import serializers
from users.models import User
from equipos.apiequipos.serializers import EquipoSerializer



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']




    def create(self, validated_data): # Sobreescribimos el metodo create para que el password sea encriptado
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    


class UserSerializer(serializers.ModelSerializer):
    equipo = EquipoSerializer()
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'equipo']




class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'equipo']