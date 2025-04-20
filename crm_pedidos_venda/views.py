from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import JsonResponse
from core import metricas
from crm_veiculos.models import Veiculos
from .forms import PedidoVendaForm
from . import forms
from . import models

class PedidoVendaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.PedidosVenda
    template_name = 'pedido_venda_list.html'
    context_object_name = 'pedidos_venda'
    paginate_by = 10
    permission_required = 'crm_pedidos_venda.view_pedidosvenda'

    def get_queryset(self):
        queryset = super().get_queryset()

        emitente = self.request.GET.get('emitente', '')
        cliente = self.request.GET.get('cliente', '')
        veiculo = self.request.GET.get('veiculo', '')
        vendedor = self.request.GET.get('vendedor', '')
        status_financiamento = self.request.GET.get('status_financiamento', '')
        status_negociacao = self.request.GET.get('status_negociacao', '')
               
        queryset = queryset.filter(status=True)

        if emitente:
            queryset = queryset.filter(emitente__nome__icontains=emitente)

        if cliente:
            queryset = queryset.filter(cliente__nome__icontains=cliente)

        if veiculo:
        # Supondo que 'descricao' seja o campo no modelo relacionado `Modelos`
         queryset = queryset.filter(veiculo__modelo__descricao__icontains=veiculo)

        if vendedor:
         queryset = queryset.filter(vendedor__nome__icontains=vendedor)

        if status_financiamento:
            queryset = queryset.filter(status_financiamento=status_financiamento)

        if status_negociacao:
            queryset = queryset.filter(status_negociacao=status_negociacao)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'emitente': self.request.GET.get('emitente', ''),
            'cliente': self.request.GET.get('cliente', ''),
            'veiculo': self.request.GET.get('veiculo', ''),
            'vendedor': self.request.GET.get('vendedor', ''),
            'status_financiamento': self.request.GET.get('status_financiamento', ''),
            'status_negociacao': self.request.GET.get('status_negociacao', ''),
        }  
        
        # Corrigir o nome da variável para corresponder ao que o template espera
        context['status_financiamento_choices'] = PedidoVendaForm.STATUS_FINANCIAMENTO_CHOICES
        context['status_negociacao_choices'] = PedidoVendaForm.STATUS_NEGOCIACAO_CHOICES

        #adiciona as metricas do painel
        context['metricas_pedidos_venda'] = metricas.get_metricas_pedidos_venda

        context['total_registros'] = self.get_queryset().count()
        
        return context

class PedidoVendaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.PedidosVenda
    template_name = 'pedido_venda_create.html'
    form_class = forms.PedidoVendaForm
    success_url = reverse_lazy('pedido_venda_list')
    permission_required = 'crm_pedidos_venda.add_pedidosvenda'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Pedido de Venda cadastrado com sucesso!')
        return response

class PedidoVendaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.PedidosVenda
    template_name = 'pedido_venda_detail.html'
    permission_required = 'crm_pedidos_venda.view_pedidosvenda'

class PedidoVendaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.PedidosVenda
    template_name = 'pedido_venda_update.html'
    form_class = forms.PedidoVendaForm
    success_url = reverse_lazy('pedido_venda_list')
    permission_required = 'crm_pedidos_venda.change_pedidosvenda'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Pedido de Venda atualizado com sucesso!')
        return response

class PedidoVendaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.PedidosVenda
    template_name = 'pedido_venda_delete.html'
    success_url = reverse_lazy('pedido_venda_list')
    permission_required = 'crm_pedidos_venda.delete_pedidosvenda'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Pedido de Venda inativado com sucesso!')
        return response

def get_veiculos(request):
    emitente_id = request.GET.get('emitente')
    situacao = request.GET.get('situacao', 'ESTOQUE')  # Valor padrão 'ESTOQUE' se não for fornecido
    veiculo_atual_id = request.GET.get('veiculo_atual')  # Para caso de edição
    
    # Filtrar veículos por emitente e situação
    veiculos = Veiculos.objects.filter(
        emitente_id=emitente_id,
        situacao=situacao
    )
    
    # Se estiver editando, incluir o veículo atual mesmo que não esteja em estoque
    if veiculo_atual_id:
        veiculo_atual = Veiculos.objects.filter(id=veiculo_atual_id, emitente_id=emitente_id)
        if veiculo_atual.exists() and not veiculos.filter(id=veiculo_atual_id).exists():
            veiculos = veiculos | veiculo_atual
    
    data = [{'id': v.id, 'modelo': str(v.modelo), 'chassi': v.chassi, 'descricao': str(v)} for v in veiculos]
    print(f"Dados enviados para o cliente: {len(data)} veículos do emitente {emitente_id} com situação '{situacao}'")
    return JsonResponse(data, safe=False)