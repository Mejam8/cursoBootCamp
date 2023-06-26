from django.http import HttpResponse
from django.shortcuts import render

from catalogo.models import Director, Peliculas


def buscar_director(request):
    directores = Director.objects.all()
    context = {
        "directores": directores
    }

    return render(request, "base.html", context)
