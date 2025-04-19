from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models


class FamiliaProdutoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.FamiliasProduto
    template_name = 'familia_produto_list.html'
    context_object_name = 'familias_produto'
    paginate_by = 10
    permission_required = 'familias_produto.view_familias_produto'

    def get_queryset(self):
        queryset = super().get_queryset()

        descricao = self.request.GET.get('descricao', '')
        produto = self.request.GET.get('produto', '')
        
        queryset = queryset.filter(status=True)

        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao) 
            
        if produto:
            queryset = queryset.filter(produto__descricao__icontains=produto)       
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'descricao': self.request.GET.get('descricao', ''),
            'produto': self.request.GET.get('produto', ''),            
        }     

        context['total_registros'] = self.get_queryset().count()
        
        return context

class FamiliaProdutoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.FamiliasProduto
    template_name = 'familia_produto_create.html'
    form_class = forms.FamiliaProdutoForm
    success_url = reverse_lazy('familia_produto_list')
    permission_required = 'crm_familias_produto.add_familiasproduto'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Familia do produto cadastrada com sucesso!')
        return response

class FamiliaProdutoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.FamiliasProduto
    template_name = 'familia_produto_detail.html'
    permission_required = 'crm_familias_produto.view_familiasproduto'

class FamiliaProdutoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.FamiliasProduto
    template_name = 'familia_produto_update.html'
    form_class = forms.FamiliaProdutoForm
    success_url = reverse_lazy('familia_produto_list')
    permission_required = 'crm_familias_produto.change_familiasproduto'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Familia do Produto atualizada com sucesso!')
        return response

class FamiliaProdutoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.FamiliasProduto
    template_name = 'familia_produto_delete.html'
    success_url = reverse_lazy('familia_produto_list')
    permission_required = 'crm_familias_produto.delete_familiasproduto'    

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Familia do Produto inativada com sucesso!')
        return response

