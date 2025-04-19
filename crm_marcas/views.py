from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class MarcaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Marcas
    template_name = 'marca_list.html'
    context_object_name = 'marcas'
    paginate_by = 10
    permission_required = 'crm_marcas.view_marcas'

    def get_queryset(self):
        queryset = super().get_queryset()

        descricao = self.request.GET.get('descricao', '')
        sigla = self.request.GET.get('sigla', '')
        
        queryset = queryset.filter(status=True)

        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao) 
            
        if sigla:
            queryset = queryset.filter(sigla__icontains=sigla)       
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'cidade': self.request.GET.get('cidade', ''),
            'regiao': self.request.GET.get('regiao', ''),            
        }     

        context['total_registros'] = self.get_queryset().count()
        
        return context

class MarcaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Marcas
    template_name = 'marca_create.html'
    form_class = forms.MarcaForm
    success_url = reverse_lazy('marca_list')
    permission_required = 'crm_marcas.add_marcas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Marca cadastrada com sucesso!')
        return response

class MarcaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Marcas
    template_name = 'marca_detail.html'
    permission_required = 'crm_marcas.view_marcas'

class MarcaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Marcas
    template_name = 'marca_update.html'
    form_class = forms.MarcaForm
    success_url = reverse_lazy('marca_list')
    permission_required = 'crm_marcas.change_marcas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Marca atualizada com sucesso!')
        return response

class MarcaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Marcas
    template_name = 'marca_delete.html'
    success_url = reverse_lazy('marca_list')
    permission_required = 'crm_marcas.delete_marcas'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Marca inativada com sucesso!')
        return response
