from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)

    def __str__(self):
        return f"{self.nome} ({self.cnpj})"

class Regional(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class RegistroHora(models.Model):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f'{self.regional} - {self.data}'


    def total_horas(self):
        delta = datetime.combine(self.data, self.hora_fim) - datetime.combine(self.data, self.hora_inicio)
        return delta.total_seconds() / 3600

class Gestão(models.Model):
    regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.regional} - {self.email} - {self.nome}'

class fiscais(models.Model):
    regional = models.ForeignKey(Regional, on_delete= models.CASCADE)
    email = models.CharField(max_length = 100)
    nome = models.CharField(max_length= 100)

    def __str__(self):
        return f'{self.regional} - {self.email} - {self.nome}'

class Perfil(models.Model):
    TIPOS_USUARIO = [
        ('funcionario', 'Funcionário'),
        ('gestor', 'Gestor'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS_USUARIO)
    regional = models.ForeignKey('Regional', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.tipo}'

class AtividadeHoraExtra(models.Model):
    gestor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='atividades_criadas')
    regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    ocupada = models.BooleanField(default=False)
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='atividades_assumidas')

    def __str__(self):
        return f"{self.descricao} - {self.data} ({'Ocupada' if self.ocupada else 'Disponível'})"

    def total_horas(self):
        delta = datetime.combine(self.data, self.hora_fim) - datetime.combine(self.data, self.hora_inicio)
        return delta.total_seconds() / 3600

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
