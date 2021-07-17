from django.db import models


# This class is for departament names
class Departamento(models.Model):
    nome_departamento = models.CharField(max_length=100, help_text='Digite o nome do departamento')
    descricao_do_departamento = models.TextField(help_text='Faça uma breve descriçao sobre o departamento')
    slug = models.SlugField(max_length=100, unique=True, null=True, help_text='Padrão de referencia')
    data_modificaao = models.DateTimeField(auto_now=True, help_text='Data da criação do arquivo')
    data_criacao = models.DateTimeField(auto_now_add=True, help_text='Data da criação do arquivo')

    def __str__(self):
        return self.nome_departamento
