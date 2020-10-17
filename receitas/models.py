from django.db import models
from datetime import datetime


class Receita(models.Model):
    nome_receita = models.CharField(
        max_length=200, verbose_name='nome da receita')
    ingredientes = models.TextField()
    modo_preparo = models.TextField(verbose_name='modo de preparo')
    tempo_preparo = models.IntegerField(verbose_name='tempo de preparo')
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(
        default=datetime.now, verbose_name='data da receita', blank=True)
