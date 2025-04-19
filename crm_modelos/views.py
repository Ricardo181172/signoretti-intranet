from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models
from decimal import Decimal

class ModeloListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Modelos
    template_name = 'modelo_list.html'
    context_object_name = 'modelos'
    paginate_by = 10
    permission_required = 'crm_modelos.view_modelos'


    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Parâmetros de filtro
        descricao = self.request.GET.get('descricao', '')
        marca = self.request.GET.get('marca', '')
        familia_produto = self.request.GET.get('familia_produto', '')       
        
        # Filtra os registros onde status é True
        queryset = queryset.filter(status=True)

        # Aplica os filtros se os parâmetros forem fornecidos
        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)
        
        if marca:
            queryset = queryset.filter(marca__sigla__icontains=marca)    
        
        if familia_produto:
            queryset = queryset.filter(familia_produto__descricao__icontains=familia_produto)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
    # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'descricao': self.request.GET.get('descricao', ''),
            'marca': self.request.GET.get('marca', ''),
            'familia_produto': self.request.GET.get('familia_produto', ''),
        }  
        
        # Adicionar o total de registros
        context['total_registros'] = self.get_queryset().count()
        
        return context    

class ModeloCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Modelos
    template_name = 'modelo_create.html'
    form_class = forms.ModeloForm
    success_url = reverse_lazy('modelo_list')
    permission_required = 'crm_modelos.add_modelos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Modelo cadastrado com sucesso!')
        return response

class ModeloDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Modelos
    template_name = 'modelo_detail.html'
    permission_required = 'crm_modelos.view_modelos'

class ModeloUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Modelos
    template_name = 'modelo_update.html'
    form_class = forms.ModeloForm
    success_url = reverse_lazy('modelo_list')
    permission_required = 'crm_modelos.change_modelos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Modelo atualizado com sucesso!')
        return response

class ModeloDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Modelos
    template_name = 'modelo_delete.html'
    success_url = reverse_lazy('modelo_list')
    permission_required = 'crm_modelos.delete_modelos'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Modelo inativado com sucesso!')
        return response
