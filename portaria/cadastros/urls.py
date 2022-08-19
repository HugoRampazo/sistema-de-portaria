from django.urls import path
from .views import CasaCreate, CasaUpdate, CasaDelete, CasaList
from .views import MoradorCreate, MoradorUpdate, MoradorDelete, MoradorList
from .views import VisitanteCreate, VisitanteUpdate, VisitanteDelete, VisitanteList
from .views import PrestadorServicoCreate, PrestadorServicoUpdate, PrestadorServicoDelete, PrestadorServicoList

urlpatterns = [
    path('cadastrar/casa/', CasaCreate.as_view(), name='cadastrar-casa'),
    path('editar/casa/<int:pk>/', CasaUpdate.as_view(), name='editar-casa'),
    path('excluir/casa/<int:pk>/', CasaDelete.as_view(), name='excluir-casa'),
    path('listar/casas/', CasaList.as_view(), name='listar-casas'),

    path('cadastrar/morador/', MoradorCreate.as_view(), name='cadastrar-morador'),
    path('editar/morador/<int:pk>/', MoradorUpdate.as_view(), name='editar-morador'),
    path('excluir/morador/<int:pk>/', MoradorDelete.as_view(), name='excluir-morador'),
    path('listar/moradores/', MoradorList.as_view(), name='listar-moradores'),

    path('cadastrar/visitante/', VisitanteCreate.as_view(), name='cadastrar-visitante'),
    path('editar/visitante/<int:pk>/', VisitanteUpdate.as_view(), name='editar-visitante'),
    path('excluir/visitante/<int:pk>/', VisitanteDelete.as_view(), name='excluir-visitante'),
    path('listar/visitantes/', VisitanteList.as_view(), name='listar-visitantes'),

    path('cadastrar/prestador_servico/', PrestadorServicoCreate.as_view(), name='cadastrar-prestador'),
    path('editar/prestador_servico/<int:pk>/', PrestadorServicoUpdate.as_view(), name='editar-prestador'),
    path('excluir/prestador/<int:pk>/', PrestadorServicoDelete.as_view(), name='excluir-prestador'),
    path('listar/prestadores_servicos/', PrestadorServicoList.as_view(), name='listar-prestadores'),

]