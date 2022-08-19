from django.urls import path
from .views import PaginaInicial, MapaCondominio

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('mapadocondominio/', MapaCondominio.as_view(), name='mapacondominio'),
]