
from django.urls import path

from catalogo.views import buscar_director

urlpatterns = [
    path('', buscar_director),
]

