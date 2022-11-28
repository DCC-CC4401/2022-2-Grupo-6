from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    pass

class Oferta(models.Model):
    p_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                        null = True, 
                        on_delete = models.SET_NULL,
                        db_column="p_user"
                        )

    CATEGORIES = ['nameTutor','titulo','materia','contacto','descripcion'
    ]
    nameTutor = models.CharField(max_length=255, null = False)
    titulo = models.CharField(max_length=255, null = False)
    materia = models.CharField(max_length=255, null = False)
    contacto=models.CharField(max_length=255, null = False)
    descripcion = models.CharField(max_length=255, null = False)
    
   
    class Meta:
        db_table = 'oferta'