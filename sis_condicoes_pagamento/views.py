from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class CondicaoPagamentoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.CondicoesPagamento
    template_name = 'condicao_pagamento_list.html'
    context_object_name = 'condicoes_pagamento'
    paginate_by = 10
    permission_required = 'crm_condicoes_pagamento.view_condicoespagamento'

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

class CondicaoPagamentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.CondicoesPagamento
    template_name = 'condicao_pagamento_create.html'
    form_class = forms.CondicaoPagamentoForm
    success_url = reverse_lazy('condicao_pagamento_list')
    permission_required = 'crm_condicoes_pagamento.add_condicoespagamento'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Condição de Pagamento cadastrada com sucesso!')
        return response

class CondicaoPagamentoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.CondicoesPagamento
    template_name = 'condicao_pagamento_detail.html'
    permission_required = 'crm_condicoes_pagamento.view_condicoespagamento'

class CondicaoPagamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.CondicoesPagamento
    template_name = 'condicao_pagamento_update.html'
    form_class = forms.CondicaoPagamentoForm
    success_url = reverse_lazy('condicao_pagamento_list')
    permission_required = 'crm_condicoes_pagamento.change_condicoespagamento'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Condição de Pagamento atualizada com sucesso!')
        return response

class CondicaoPagamentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.CondicoesPagamento
    template_name = 'condicao_pagamento_delete.html'
    success_url = reverse_lazy('condicao_pagamento_list')
    permission_required = 'crm_condicoes_pagamento.delete_condicoespagamento'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Condição de Pagamento inativada com sucesso!')
        return response
