from django.db import models
from django.contrib.auth.models import User
import datetime

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)

    def __str__(self):
        return f"{self.nome} ({self.cnpj})"

class Regional (models.Model):
    nome = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class RegistroHora(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.usuario} - {self.regional} - {self.data}"

    def total_horas(self):
        delta = datetime.combine(self.data, self.hora_fim) - datetime.combine(self.data, self.hora_inicio)
        return delta.total_seconds() / 3600
