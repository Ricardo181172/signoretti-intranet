from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models


class ProdutoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Produtos
    template_name = 'produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 10
    permission_required = 'crm_produtos.view_produtos'

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
            'descricao': self.request.GET.get('descricao', ''),
            'sigla': self.request.GET.get('sigla', ''),            
        }     

        context['total_registros'] = self.get_queryset().count()
        
        return context

class ProdutoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Produtos
    template_name = 'produto_create.html'
    form_class = forms.ProdutoForm
    success_url = reverse_lazy('produto_list')
    permission_required = 'crm_produtos.add_produtos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return response

class ProdutoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Produtos
    template_name = 'produto_detail.html'
    permission_required = 'crm_produtos.view_produtos'

class ProdutoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Produtos
    template_name = 'produto_update.html'
    form_class = forms.ProdutoForm
    success_url = reverse_lazy('produto_list')
    permission_required = 'crm_produtos.change_produtos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return response

class ProdutoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Produtos
    template_name = 'produto_delete.html'
    success_url = reverse_lazy('produto_list')
    permission_required = 'crm_produtos.delete_produtos'
   
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Produto inativado com sucesso!')
        return response
