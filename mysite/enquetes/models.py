import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("date piblished")


class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)




