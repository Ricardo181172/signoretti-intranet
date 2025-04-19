from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class CulturaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Culturas
    template_name = 'cultura_list.html'
    context_object_name = 'culturas'
    paginate_by = 10
    permission_required = 'crm_culturas.view_culturas'

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

class CulturaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Culturas
    template_name = 'cultura_create.html'
    form_class = forms.CulturaForm
    success_url = reverse_lazy('cultura_list')
    permission_required = 'crm_culturas.add_culturas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cultura cadastrada com sucesso!')
        return response

class CulturaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Culturas
    template_name = 'cultura_detail.html'
    permission_required = 'crm_culturas.view_culturas'

class CulturaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Culturas
    template_name = 'cultura_update.html'
    form_class = forms.CulturaForm
    success_url = reverse_lazy('cultura_list')
    permission_required = 'crm_culturas.change_culturas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cultura atualizada com sucesso!')
        return response

class CulturaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Culturas
    template_name = 'cultura_delete.html'
    success_url = reverse_lazy('cultura_list')
    permission_required = 'crm_culturas.delete_culturas'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Cultura inativada com sucesso!')
        return response
