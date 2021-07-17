from django.contrib import admin
from apps.registro_hora_extra.models import RegistroHoraExtra


@admin.register(RegistroHoraExtra)
class RegistroHoraExtraAdmin(admin.ModelAdmin):
    list_display = ("hora_extra", "motivo_hora_extra", "pertence_a", "data_hora_inicio",
                    "data_hora_final", "slug", "data_modificaao", "data_criacao")
    prepopulated_fields = {"slug": ("hora_extra",)}