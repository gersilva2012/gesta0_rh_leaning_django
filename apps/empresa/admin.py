from django.contrib import admin
from apps.empresa.models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nome_da_empresa", "descricao_da_empresa", "slug", "data_modificaao", "data_criacao")
    prepopulated_fields = {"slug": ("nome_da_empresa",)}
