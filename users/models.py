import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from equipos.models import Equipo


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True, related_name='miembros')

    


    USERNAME_FIELD = 'email' # Mediante esta config pediremos como parametro de entrada el email y password en el panel de administración
    REQUIRED_FIELDS = []
