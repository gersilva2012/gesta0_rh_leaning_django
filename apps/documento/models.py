from django.db import models
from apps.colaborador.models import Colaborador


# Create your models here.
class Documento(models.Model):
    nome_documento = models.CharField(max_length=100, help_text="Nome do documento")
    descricao_do_documento = models.TextField(help_text="Faça uma breve descrição sobre este documento")
    a_quem_pertence = models.ForeignKey(Colaborador, on_delete=models.PROTECT, related_name='pertence_a',
                                        help_text='A quem pertence o arquivo')
    slug = models.SlugField(max_length=100, unique=True, null=True, help_text='Padrão de referencia')
    data_modificaao = models.DateTimeField(auto_now=True, help_text='Data da criação do arquivo')
    data_criacao = models.DateTimeField(auto_now_add=True, help_text='Data da criação do arquivo')

    def __str__(self):
        return f'{self.nome_documento} {" - Descrição:"} {self.descricao_do_documento}'
