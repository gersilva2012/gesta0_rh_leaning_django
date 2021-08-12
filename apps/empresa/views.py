# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Empresa


# @login_required
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome_empresa', 'descricao_da_empresa',]
