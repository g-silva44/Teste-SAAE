from django.db import models
from django.contrib.auth.models import User

class Bairro(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome do Bairro')

    # Campos para o recurso de mapa
    latitude = models.FloatField(default=-9.4137, verbose_name='Latitude')
    longitude = models.FloatField(default=-40.5036, verbose_name='Longitude')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'


    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    STATUS_CHOICES = [
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('RESOLVIDO', 'Resolvido')
    ]

    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, related_name='ocorrencias', verbose_name='Bairro')
    data_hora = models.DateTimeField(verbose_name="Data/Hora da Ocorrência")
    descricao = models.TextField(verbose_name="Descrição do Problema")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EM_ANDAMENTO', verbose_name="Status")
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Responsável")

    class Meta:
        ordering = ['-data_hora']
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'

    def __str__(self):
        return f"{self.bairro.nome} - {self.get_status_display()} ({self.data_hora.strftime('%d/%m/%Y %H:%M')})"