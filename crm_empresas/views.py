from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import JsonResponse
from django.shortcuts import redirect
from . import forms
from .forms import EmpresasForm
from . import models
from sis_cidades.models import Cidades


class EmpresaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Empresas
    template_name = 'empresa_list.html'
    context_object_name = 'empresas'
    paginate_by = 10
    permission_required = 'crm_empresas.view_empresas'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        nome = self.request.GET.get('nome', '')
        cidade = self.request.GET.get('cidade', '')
        tipo_empresa = self.request.GET.get('tipo_empresa', '')
               
        queryset = queryset.filter(status=True)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        if cidade:
            queryset = queryset.filter(cidade__municipio__icontains=cidade)     

        if tipo_empresa:
            queryset = queryset.filter(tipo_empresa=tipo_empresa) 
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {            
            'nome': self.request.GET.get('nome', ''),
            'cidade': self.request.GET.get('cidade', ''),
            'tipo_empresa': self.request.GET.get('tipo_empresa', ''),            
        } 

        context['tipo_empresa_choices'] = EmpresasForm.TIPO_EMPRESA_CHOICES      

        context['total_registros'] = self.get_queryset().count()
        
        return context

class EmpresaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Empresas
    template_name = 'empresa_create.html'
    form_class = forms.EmpresasForm
    success_url = reverse_lazy('empresa_list')
    permission_required = 'crm_empresas.add_empresas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Empresa cadastrada com sucesso!')
        return response

class EmpresaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Empresas
    template_name = 'empresa_detail.html'
    permission_required = 'crm_empresas.view_empresas'

class EmpresaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Empresas
    template_name = 'empresa_update.html'
    form_class = forms.EmpresasForm
    success_url = reverse_lazy('empresa_list')
    permission_required = 'crm_empresas.change_empresas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Empresa atualizada com sucesso!')
        return response

class EmpresaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Empresas
    template_name = 'empresa_delete.html'
    success_url = reverse_lazy('empresa_list')
    permission_required = 'crm_empresas.delete_empresas'
    
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()  # Agora, usa o método delete alterado do modelo
        return redirect(self.success_url)

def get_cidades(request, uf):
    cidades = Cidades.objects.filter(uf=uf).values('id', 'municipio')
    return JsonResponse({'cidades': list(cidades)})
