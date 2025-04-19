from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class TipoMetaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.TiposMeta
    template_name = 'tipo_meta_list.html'
    context_object_name = 'tipos_meta'
    paginate_by = 10
    permission_required = 'crm_tipos_meta.view_tiposmeta'

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

class TipoMetaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.TiposMeta
    template_name = 'tipo_meta_create.html'
    form_class = forms.TipoMetaForm
    success_url = reverse_lazy('tipo_meta_list')
    permission_required = 'crm_tipos_meta.add_tiposmeta'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Tipo de Meta cadastrada com sucesso!')
        return response

class TipoMetaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.TiposMeta
    template_name = 'tipo_meta_detail.html'
    permission_required = 'crm_tipos_meta.view_tiposmeta'

class TipoMetaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.TiposMeta
    template_name = 'tipo_meta_update.html'
    form_class = forms.TipoMetaForm
    success_url = reverse_lazy('tipo_meta_list')
    permission_required = 'crm_tipos_meta.change_tiposmeta'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Tipo de Meta atualizada com sucesso!')
        return response

class TipoMetaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.TiposMeta
    template_name = 'tipo_meta_delete.html'
    success_url = reverse_lazy('tipo_meta_list')
    permission_required = 'crm_tipos_meta.delete_tiposmeta'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Tipo de Meta inativada com sucesso!')
        return response
