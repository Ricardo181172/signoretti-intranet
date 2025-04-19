from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class ConfiguracaoVeiculoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.ConfiguracoesVeiculo
    template_name = 'configuracao_veiculo_list.html'
    context_object_name = 'configuracoes_veiculo'
    paginate_by = 10
    permission_required = 'crm_configuracoes_veiculo.view_configuracoesveiculo'

    def get_queryset(self):
        queryset = super().get_queryset()

        modelo = self.request.GET.get('modelo', '')
        top_cat = self.request.GET.get('top_cat', '') 
        acessorio = self.request.GET.get('acessorio', '')
        
        queryset = queryset.filter(status=True)

        if modelo:           
            queryset = queryset.filter(modelo__descricao__icontains=modelo)
            
        if top_cat:
            queryset = queryset.filter(top_cat__icontains=top_cat)

        if acessorio:
            queryset = queryset.filter(acessorio__descricao__icontains=acessorio)       
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'modelo': self.request.GET.get('modelo', ''),
            'top_cat': self.request.GET.get('top_cat', ''),
            'acessorio': self.request.GET.get('acessorio', ''),            
        }     

        context['total_registros'] = self.get_queryset().count()
        
        return context

class ConfiguracaoVeiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.ConfiguracoesVeiculo
    template_name = 'configuracao_veiculo_create.html'
    form_class = forms.ConfiguracaoVeiculoForm
    success_url = reverse_lazy('configuracao_veiculo_list')
    permission_required = 'crm_configuracoes_veiculo.add_configuracoesveiculo'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Configuração de veículo cadastrado com sucesso!')
        return response

class ConfiguracaoVeiculoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.ConfiguracoesVeiculo
    template_name = 'configuracao_veiculo_detail.html'
    permission_required = 'crm_configuracoes_veiculo.view_configuracoesveiculo'

class ConfiguracaoVeiculoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.ConfiguracoesVeiculo
    template_name = 'configuracao_veiculo_update.html'
    form_class = forms.ConfiguracaoVeiculoForm
    success_url = reverse_lazy('configuracao_veiculo_list')
    permission_required = 'crm_configuracoes_veiculo.change_configuracoesveiculo'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Configuração de veículo atualizado com sucesso!')
        return response

class ConfiguracaoVeiculoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.ConfiguracoesVeiculo
    template_name = 'configuracao_veiculo_delete.html'
    success_url = reverse_lazy('configuracao_veiculo_list')
    permission_required = 'crm_configuracoes_veiculo.delete_configuracoesveiculo'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Configuração de veículo inativado com sucesso!')
        return response
