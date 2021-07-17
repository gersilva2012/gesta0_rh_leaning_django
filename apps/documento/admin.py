from django.contrib import admin
from .models import Documento


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    ist_display = ("nome_documento", "descricao_do_documento", "slug", "data_modificaao", "data_criacao")
    prepopulated_fields = {"slug": ("nome_documento",)}
