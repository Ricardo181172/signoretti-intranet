from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models


class VendaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Vendas
    template_name = 'venda_list.html'
    context_object_name = 'vendas'
    paginate_by = 10 
    permission_required = 'crm_vendas.view_vendas'   

    def get_queryset(self):
        queryset = super().get_queryset()
        pedido_venda = self.request.GET.get('pedido_venda')

        # Filtra os registros onde status é True
        queryset = queryset.filter(status=True)

        if pedido_venda:
            queryset = queryset.filter(pedido_venda__icontains=pedido_venda)
        
        return queryset

class VendaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Vendas
    template_name = 'venda_create.html'
    form_class = forms.VendaForm
    success_url = reverse_lazy('venda_list')
    permission_required = 'crm_vendas.add_vendas'   

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cidade Região cadastrada com sucesso!')
        return response

class VendaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Vendas
    template_name = 'venda_detail.html'
    permission_required = 'crm_vendas.view_vendas'   

class VendaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Vendas
    template_name = 'venda_update.html'
    form_class = forms.VendaForm
    success_url = reverse_lazy('venda_list')
    permission_required = 'crm_vendas.change_vendas'   

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cidade Região atualizada com sucesso!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar a cidade região. Por favor, verifique os campos.')
        return super().form_invalid(form)

class VendaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Vendas
    template_name = 'venda_delete.html'
    success_url = reverse_lazy('venda_list')
    permission_required = 'crm_vendas.delete_vendas'      

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Cidade Região inativada com sucesso!')
        return response
