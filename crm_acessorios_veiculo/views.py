from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import JsonResponse
from . import forms
from . import models

class AcessorioVeiculoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):   
    model = models.AcessoriosVeiculo
    template_name = 'acessorio_veiculo_list.html'
    context_object_name = 'acessorios_veiculo'
    paginate_by = 10
    permission_required = 'crm_acessorios_veiculo.view_acessoriosveiculo'

    def get_queryset(self):
        queryset = super().get_queryset()

        descricao = self.request.GET.get('descricao', '')        
               
        queryset = queryset.filter(status=True)

        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'descricao': self.request.GET.get('descricao', ''),            
        }         
       
        context['total_registros'] = self.get_queryset().count()
        
        return context
    
class AcessorioVeiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.AcessoriosVeiculo
    template_name = 'acessorio_veiculo_create.html'
    form_class = forms.AcessorioVeiculoForm
    success_url = reverse_lazy('acessorio_veiculo_list')
    permission_required = 'crm_acessorios_veiculo.add_acessoriosveiculo'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acessorio de veículo cadastrado com sucesso!')
        return response

class AcessorioVeiculoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.AcessoriosVeiculo
    template_name = 'acessorio_veiculo_detail.html'
    permission_required = 'crm_acessorios_veiculo.view_acessoriosveiculo'

class AcessorioVeiculoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.AcessoriosVeiculo
    template_name = 'acessorio_veiculo_update.html'
    form_class = forms.AcessorioVeiculoForm
    success_url = reverse_lazy('acessorio_veiculo_list')
    permission_required = 'crm_acessorios_veiculo.change_acessoriosveiculo'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acessorio de veículo atualizado com sucesso!')
        return response

class AcessorioVeiculoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.AcessoriosVeiculo
    template_name = 'acessorio_veiculo_delete.html'
    success_url = reverse_lazy('acessorio_veiculo_list')
    permission_required = 'crm_acessorios_veiculo.delete_acessoriosveiculo'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Acessorio de veículo inativado com sucesso!')
        return response
