from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from . import forms
from . import models
from sis_cidades.models import Cidades


class CidadeRegiaoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.CidadesRegiao
    template_name = 'cidade_regiao_list.html'
    context_object_name = 'cidades_regiao'
    paginate_by = 10
    permission_required = 'crm_cidades_regiao.view_cidadesregiao'

    def get_queryset(self):
        queryset = super().get_queryset()

        cidade = self.request.GET.get('cidade', '')
        regiao = self.request.GET.get('regiao', '')
        
        queryset = queryset.filter(status=True)

        if cidade:
            queryset = queryset.filter(cidade__municipio__icontains=cidade) 
            
        if regiao:
            queryset = queryset.filter(regiao__descricao__icontains=regiao)       
            
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

class CidadeRegiaoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.CidadesRegiao
    template_name = 'cidade_regiao_create.html'
    form_class = forms.CidadeRegiaoForm
    success_url = reverse_lazy('cidade_regiao_list')
    permission_required = 'crm_cidades_regiao.add_cidadesregiao'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cidade Região cadastrada com sucesso!')
        return response

class CidadeRegiaoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.CidadesRegiao
    template_name = 'cidade_regiao_detail.html'
    permission_required = 'crm_cidades_regiao.view_cidadesregiao'

class CidadeRegiaoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.CidadesRegiao
    template_name = 'cidade_regiao_update.html'
    form_class = forms.CidadeRegiaoForm
    success_url = reverse_lazy('cidade_regiao_list')
    permission_required = 'crm_cidades_regiao.change_cidadesregiao'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cidade Região atualizada com sucesso!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar a cidade região. Por favor, verifique os campos.')
        return super().form_invalid(form)

class CidadeRegiaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.CidadesRegiao
    template_name = 'cidade_regiao_delete.html'
    success_url = reverse_lazy('cidade_regiao_list')
    permission_required = 'crm_cidades_regiao.delete_cidadesregiao'  

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Cidade Região inativada com sucesso!')
        return response

def get_cidades(request, uf):
    cidades = Cidades.objects.filter(uf=uf).values('id', 'municipio')
    return JsonResponse({'cidades': list(cidades)})
