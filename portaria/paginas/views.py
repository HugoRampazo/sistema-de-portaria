from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

class MapaCondominio(TemplateView):
    template_name = 'paginas/mapa.html'