from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class RegiaoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Regioes
    template_name = 'regiao_list.html'
    context_object_name = 'regioes'
    paginate_by = 10
    permission_required = 'crm_regioes.view_regioes'

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

class RegiaoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Regioes
    template_name = 'regiao_create.html'
    form_class = forms.RegiaoForm
    success_url = reverse_lazy('regiao_list')
    permission_required = 'crm_regioes.add_regioes'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Região cadastrada com sucesso!')
        return response

class RegiaoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Regioes
    template_name = 'regiao_detail.html'
    permission_required = 'crm_regioes.view_regioes'

class RegiaoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Regioes
    template_name = 'regiao_update.html'
    form_class = forms.RegiaoForm
    success_url = reverse_lazy('regiao_list')
    permission_required = 'crm_regioes.change_regioes'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Região atualizada com sucesso!')
        return response

class RegiaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Regioes
    template_name = 'regiao_delete.html'
    success_url = reverse_lazy('regiao_list')
    permission_required = 'crm_regioes.delete_regioes'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Região inativada com sucesso!')
        return response
