from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class TipoComissaoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.TiposComissao
    template_name = 'tipo_comissao_list.html'
    context_object_name = 'tipos_comissao'
    paginate_by = 10
    permission_required = 'crm_tipos_comissao.view_tiposcomissao'

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

class TipoComissaoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.TiposComissao
    template_name = 'tipo_comissao_create.html'
    form_class = forms.TipoComissaoForm
    success_url = reverse_lazy('tipo_comissao_list')
    permission_required = 'crm_tipos_comissao.add_tiposcomissao'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Tipo de comissão cadastrada com sucesso!')
        return response

class TipoComissaoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.TiposComissao
    template_name = 'tipo_comissao_detail.html'
    permission_required = 'crm_tipos_comissao.view_tiposcomissao'

class TipoComissaoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.TiposComissao
    template_name = 'tipo_comissao_update.html'
    form_class = forms.TipoComissaoForm
    success_url = reverse_lazy('tipo_comissao_list')
    permission_required = 'crm_tipos_comissao.change_tiposcomissao'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Tipo de comissão atualizada com sucesso!')
        return response

class TipoComissaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.TiposComissao
    template_name = 'tipo_comissao_delete.html'
    success_url = reverse_lazy('tipo_comissao_list')
    permission_required = 'crm_tipos_comissao.delete_tiposcomissao'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Tipo de comissão inativada com sucesso!')
        return response
