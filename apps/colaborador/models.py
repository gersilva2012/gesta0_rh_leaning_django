from django.db import models
from django.contrib.auth.models import User
from apps.empresa.models import Empresa
from apps.departamento.models import Departamento


# my class for created users.
class Colaborador(models.Model):
    nome_colaborador = models.CharField(max_length=100, help_text='Nome do colaboradores')
    nome_usuario = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_name_test')
    trabalha_na_empresa = models.ForeignKey(Empresa, null=True, on_delete=models.PROTECT, related_name='onde_trabalha',
                                            help_text='Em qual empresa o colaborador trabalha')
    no_setor = models.ForeignKey(Departamento, null=True, on_delete=models.PROTECT, related_name='em_qual_setor',
                                 help_text='Em qual setor')
    slug = models.SlugField(max_length=100, unique=True, null=True, help_text='Padrão de referencia')
    data_modificaao = models.DateTimeField(auto_now=True, help_text='Data da criação do arquivo')
    data_criacao = models.DateTimeField(auto_now_add=True, help_text='Data da criação do arquivo')

    def __str__(self):
        return self.nome_colaborador
