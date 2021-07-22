from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Não digita nada então leva a apps.core.urls.py
    path('', include('apps.core.urls')),
    path('colaborador/', include('apps.colaborador.urls')),
    path('departamento/', include('apps.departamento.urls')),
    path('documento/', include('apps.documento.urls')),
    path('empresa/', include('apps.empresa.urls')),
    path('registro_hora_extra/', include('apps.registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    # Nos mostra as informações de login e logout
    path('accounts/', include('django.contrib.auth.urls')),
]
