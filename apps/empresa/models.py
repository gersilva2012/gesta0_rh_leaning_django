from django.db import models


# Create your models here.
class Empresa(models.Model):
    nome_da_empresa = models.CharField(max_length=100, help_text='Digite o nome da empresa')
    descricao_da_empresa = models.TextField(help_text='Faça uma breve descrição sobre a empresa')
    slug = models.SlugField(max_length=100, unique=True, null=True, help_text='Padrão de referencia')
    data_modificaao = models.DateTimeField(auto_now=True, help_text='Data da criação do arquivo')
    data_criacao = models.DateTimeField(auto_now_add=True, help_text='Data da criação do arquivo')

    def __str__(self):
        return self.nome_da_empresa
