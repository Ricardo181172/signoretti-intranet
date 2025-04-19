from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Clientes, Cidades
from .forms import ClienteForm
from . import forms
from . import models
from sis_cidades.models import Cidades


class ClienteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Clientes
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10
    permission_required = 'crm_clientes.view_clientes'

    def get_queryset(self):
        queryset = super().get_queryset()

        emitente = self.request.GET.get('emitente', '')
        nome = self.request.GET.get('nome', '')
        cidade = self.request.GET.get('cidade', '')
        cpf_cnpj = self.request.GET.get('cpf_cnpj', '')
        vendedor = self.request.GET.get('vendedor', '')
        status_relacionamento = self.request.GET.get('status_relacionamento', '')
               
        queryset = queryset.filter(status=True)

        if emitente:
            queryset = queryset.filter(emitente__nome__icontains=emitente)
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        if cidade:
            queryset = queryset.filter(cidade__municipio__icontains=cidade) 

        if cpf_cnpj:
            queryset = queryset.filter(cpf_cnpj__icontains=cpf_cnpj)

        if vendedor:
         queryset = queryset.filter(vendedor__nome__icontains=vendedor)

        if status_relacionamento:
            queryset = queryset.filter(status_relacionamento=status_relacionamento)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'emitente': self.request.GET.get('emitente', ''),
            'nome': self.request.GET.get('nome', ''),
            'cidade': self.request.GET.get('cidade', ''),
            'cpf_cnpj': self.request.GET.get('cpf_cnpj', ''),
            'vendedor': self.request.GET.get('vendedor', ''),
            'status_relacionamento': self.request.GET.get('status_relacionamento', ''),
        }      

        context['total_registros'] = self.get_queryset().count()
        
        return context

class ClienteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Clientes
    template_name = 'cliente_create.html'
    form_class = forms.ClienteForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'crm_clientes.add_clientes'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente cadastrado com sucesso!')
        return response

class ClienteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Clientes
    template_name = 'cliente_detail.html'
    permission_required = 'crm_clientes.view_clientes'

class ClienteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Clientes
    template_name = 'cliente_update.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'crm_clientes.change_clientes'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar o cliente. Por favor, verifique os campos.')
        return super().form_invalid(form)

class ClienteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Clientes
    template_name = 'cliente_delete.html'
    success_url = reverse_lazy('cliente_list')
    permission_required = 'crm_clientes.delete_clientes'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Cliente inativado com sucesso!')
        return response

def get_cidades(request):
    uf = request.GET.get('uf')
    cidades = Cidades.objects.filter(uf=uf).values('id', 'municipio')
    return JsonResponse(list(cidades), safe=False)
