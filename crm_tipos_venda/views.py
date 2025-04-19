from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class TipoVendaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.TiposVenda
    template_name = 'tipo_venda_list.html'
    context_object_name = 'tipos_venda'
    paginate_by = 10
    permission_required = 'crm_tipos_venda.view_tiposvenda'

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

class TipoVendaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.TiposVenda
    template_name = 'tipo_venda_create.html'
    form_class = forms.TipoVendaForm
    success_url = reverse_lazy('tipo_venda_list')
    permission_required = 'crm_tipos_venda.add_tiposvenda'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Tipo de Venda cadastrada com sucesso!')
        return response

class TipoVendaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.TiposVenda
    template_name = 'tipo_venda_detail.html'
    permission_required = 'crm_tipos_venda.view_tiposvenda'

class TipoVendaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.TiposVenda
    template_name = 'tipo_venda_update.html'
    form_class = forms.TipoVendaForm
    success_url = reverse_lazy('tipo_venda_list')
    permission_required = 'crm_tipos_venda.change_tiposvenda'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Tipo de Venda atualizada com sucesso!')
        return response

class TipoVendaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.TiposVenda
    template_name = 'tipo_venda_delete.html'
    success_url = reverse_lazy('tipo_venda_list')
    permission_required = 'crm_tipos_venda.delete_tiposvenda'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Tipo de Venda inativada com sucesso!')
        return response
