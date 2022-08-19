from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Casa, Morador, Visitante, PrestadorServico
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#################### CREATE ####################

class CasaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy ('login')
    model = Casa
    fields = ['bloco_numero', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-casas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar nova Casa"
        context['botao'] = "Cadastrar"
        return context

class MoradorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy ('login')
    model = Morador
    fields = ['nome_completo', 'cpf', 'data_de_moradia', 'telefone', 'casa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-moradores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar novo Morador"
        context['botao'] = "Cadastrar"
        return context

class VisitanteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy ('login')
    model = Visitante
    fields = ['nome_completo', 'identidade', 'data_de_entrada', 'placa_veiculo', 'casa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-visitantes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar novo Visitante"
        context['botao'] = "Cadastrar"
        return context

class PrestadorServicoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy ('login')
    model = PrestadorServico
    fields = ['nome_completo', 'identidade', 'data_de_entrada', 'placa_veiculo', 'casa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-prestadores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar novo Prestador de Serviço"
        context['botao'] = "Cadastrar"
        return context

#################### UPDATE ####################

class CasaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy ('login')
    model = Casa
    fields = ['bloco_numero', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-casas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Casa"
        context['botao'] = "Salvar"
        return context

class MoradorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy ('login')
    model = Morador
    fields = ['nome_completo', 'cpf', 'data_de_moradia', 'telefone', 'casa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-moradores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Morador"
        context['botao'] = "Salvar"
        return context

class VisitanteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy ('login')
    model = Visitante
    fields = ['nome_completo', 'identidade', 'data_de_entrada', 'placa_veiculo', 'casa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-visitantes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Visitante"
        context['botao'] = "Salvar"
        return context

class PrestadorServicoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy ('login')
    model = PrestadorServico
    fields = ['nome_completo', 'identidade', 'data_de_entrada', 'placa_veiculo', 'casa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-prestadores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Prestador de Serviço"
        context['botao'] = "Salvar"
        return context

#################### DELETE ####################

class CasaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy ('login')
    model = Casa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-casas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Excluir Casa"
        context['botao'] = "Excluir"
        return context

class MoradorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy ('login')
    model = Morador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-moradores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Excluir Morador"
        context['botao'] = "Excluir"
        return context

class VisitanteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy ('login')
    model = Visitante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-visitantes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Excluir Visitante"
        context['botao'] = "Excluir"
        return context

class PrestadorServicoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy ('login')
    model = PrestadorServico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-prestadores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Excluir Prestador de Serviço"
        context['botao'] = "Excluir"
        return context

#################### LISTAS ####################

class CasaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy ('login')
    model = Casa
    template_name = 'cadastros/listas/casa.html'

class MoradorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy ('login')
    model = Morador
    template_name = 'cadastros/listas/morador.html'

class VisitanteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy ('login')
    model = Visitante
    template_name = 'cadastros/listas/visitante.html'

class PrestadorServicoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy ('login')
    model = PrestadorServico
    template_name = 'cadastros/listas/prestador_servico.html'