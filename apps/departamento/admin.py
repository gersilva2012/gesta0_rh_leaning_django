from django.contrib import admin
from .models import Departamento


# Register your models here.
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("nome_departamento", "descricao_do_departamento", "slug", "data_modificaao", "data_criacao")
    prepopulated_fields = {"slug": ("nome_departamento",)}
