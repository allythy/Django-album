from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
# Create your models here.


class Foto(models.Model):
    imagem = ImageField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.NullBooleanField(default=None, null=True)
