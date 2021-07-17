from django.contrib import admin
from .models import Colaborador


# Register your models here.
@admin.register(Colaborador)
class ColaboradoAdmin(admin.ModelAdmin):
    list_display = ("nome_colaborador", "slug", "data_modificaao", "data_criacao")
    prepopulated_fields = {"slug": ("nome_colaborador",)}
