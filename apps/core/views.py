from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.colaborador.models import Colaborador


@login_required
def home(request):
    # vamos fazer o import das informações do funcionairo
    data = {"usuario": request.user}
    return render(request, "core/index.html", data)
