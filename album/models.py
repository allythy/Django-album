from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Album(models.Model):
    nome = models.CharField(max_length=255)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.proprietario.username}'


class Foto(models.Model):
    imagem = models.ImageField()
    data = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    aprovado = models.BooleanField(default=False)
