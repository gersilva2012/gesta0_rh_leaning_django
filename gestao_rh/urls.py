from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('colaborador/', include('apps.colaborador.urls')),
    path('departamento/', include('apps.departamento.urls')),
    path('documento/', include('apps.documento.urls')),
    path('empresa/', include('apps.empresa.urls')),
    path('registro_hora_extra/', include('apps.registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
]
