from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class MetaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Metas
    template_name = 'meta_list.html'
    context_object_name = 'metas'
    paginate_by = 10
    permission_required = 'crm_metas.view_metas'


    def get_queryset(self):
        queryset = super().get_queryset()

        mes = self.request.GET.get('mes', '')
        ano = self.request.GET.get('ano', '')
        tipo_meta = self.request.GET.get('tipo_meta', '')
        vendedor = self.request.GET.get('vendedor', '')
        produto = self.request.GET.get('produto', '')
               
        queryset = queryset.filter(status=True)

        if mes:
            queryset = queryset.filter(mes__icontains=mes)

        if ano:
            queryset = queryset.filter(ano__icontains=ano)

        if tipo_meta:
            queryset = queryset.filter(tipo_meta__descricao__icontains=tipo_meta)

        if vendedor:
            queryset = queryset.filter(vendedor__nome__icontains=vendedor)

        if produto:
            queryset = queryset.filter(produto__descricao__icontains=produto)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'mes': self.request.GET.get('mes', ''),
            'ano': self.request.GET.get('ano', ''),
            'tipo_meta': self.request.GET.get('tipo_meta', ''),
            'vendedor': self.request.GET.get('vendedor', ''),
            'produto': self.request.GET.get('produto', ''),
        }       

        context['total_registros'] = self.get_queryset().count()
        
        return context

class MetaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Metas
    template_name = 'meta_create.html'
    form_class = forms.MetaForm
    success_url = reverse_lazy('meta_list')
    permission_required = 'crm_metas.add_metas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Meta cadastrada com sucesso!')
        return response

class MetaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Metas
    template_name = 'meta_detail.html'
    permission_required = 'crm_metas.view_metas'

class MetaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Metas
    template_name = 'meta_update.html'
    form_class = forms.MetaForm
    success_url = reverse_lazy('meta_list')
    permission_required = 'crm_metas.change_metas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Meta atualizada com sucesso!')
        return response

class MetaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Metas
    template_name = 'meta_delete.html'
    success_url = reverse_lazy('meta_list')
    permission_required = 'crm_metas.delete_metas'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Meta inativada com sucesso!')
        return response

