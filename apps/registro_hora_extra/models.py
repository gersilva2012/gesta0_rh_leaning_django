from django.db import models
from apps.colaborador.models import Colaborador


class RegistroHoraExtra(models.Model):
    hora_extra = models.CharField(max_length=100, help_text='Horas extras')
    motivo_hora_extra = models.TextField(help_text='Faça uma breve descrição do motivo da hora extra')
    nome_colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT, help_text='A quem pertence hora extra')
    data_hora_inicio = models.DateTimeField(help_text='Hora e data inicial')
    data_hora_final = models.DateTimeField(help_text='Hora e data final')
    slug = models.SlugField(max_length=100, unique=True, null=True, help_text='Padrão de referencia')
    data_modificaao = models.DateTimeField(auto_now=True, help_text='Data da criação do arquivo')
    data_criacao = models.DateTimeField(auto_now_add=True, help_text='Data da criação do arquivo')

    def __str__(self):
        return self.hora_extra