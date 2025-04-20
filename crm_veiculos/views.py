from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import JsonResponse
from core import metricas
from . import forms
from . import models

class VeiculoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Veiculos
    template_name = 'veiculo_list.html'
    context_object_name = 'veiculos'
    paginate_by = 10
    permission_required = 'crm_veiculos.view_veiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Parâmetros de filtro
        chassi = self.request.GET.get('chassi', '')
        emitente = self.request.GET.get('emitente', '')
        modelo = self.request.GET.get('modelo', '')
        estado = self.request.GET.get('estado', '')
        situacao = self.request.GET.get('situacao', '')        
        
        # Filtra os registros onde status é True
        queryset = queryset.filter(status=True).filter(~Q(situacao='PAGO'))

        # Aplica os filtros se os parâmetros forem fornecidos
        if chassi:
            queryset = queryset.filter(chassi__icontains=chassi)
        
        if emitente:
            queryset = queryset.filter(emitente__nome__icontains=emitente)
        
        if modelo:
            queryset = queryset.filter(               
                Q(modelo__descricao__icontains=modelo)
            )
        
        if estado:
            queryset = queryset.filter(estado=estado)
            
        if situacao:
            queryset = queryset.filter(situacao=situacao)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
    # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'chassi': self.request.GET.get('chassi', ''),
            'emitente': self.request.GET.get('emitente', ''),
            'modelo': self.request.GET.get('modelo', ''),
            'estado': self.request.GET.get('estado', ''),
            'situacao': self.request.GET.get('situacao', ''),
        }
        
        # Adicionar as opções de estado e situação
        from .forms import VeiculoForm
        context['estado_choices'] = VeiculoForm.ESTADO_CHOICES
        context['situacao_choices'] = VeiculoForm.SITUACAO_CHOICES
        
        #adiciona as metricas do painel
        context['metricas_veiculos'] = metricas.get_metricas_veiculos
        
        # Adicionar o total de registros
        context['total_registros'] = self.get_queryset().count()
        
        return context    

class VeiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Veiculos
    template_name = 'veiculo_create.html'
    form_class = forms.VeiculoForm
    success_url = reverse_lazy('veiculo_list')
    permission_required = 'crm_veiculos.add_veiculos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Veículo cadastrado com sucesso!')
        return response

class VeiculoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Veiculos
    template_name = 'veiculo_detail.html' 
    permission_required = 'crm_veiculos.view_veiculos' 
    

class VeiculoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Veiculos
    template_name = 'veiculo_update.html'
    form_class = forms.VeiculoForm
    success_url = reverse_lazy('veiculo_list')
    permission_required = 'crm_veiculos.change_veiculos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Veículo atualizado com sucesso!')
        return response

class VeiculoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Veiculos
    template_name = 'veiculo_delete.html'
    success_url = reverse_lazy('veiculo_list')
    permission_required = 'crm_veiculos.delete_veiculos'   

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Veículo inativado com sucesso!')
        return response
    
def search_modelos(request):
    model = models.Veiculos
    nome = request.GET.get('nome', '')
    modelos = model.objects.filter(modelo__icontains=nome).values('id', 'modelo')
    data = list(modelos)
    return JsonResponse(data, safe=False)