from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Publicacion(models.Model):
    titulo = models.CharField(blank=True, null=True, max_length=250)  # un varchar
    materia = models.CharField(blank=True, null=True, max_length=250)
    horario = models.CharField(blank=True, null=True, max_length=250)
    costo = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)  # un text

    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)