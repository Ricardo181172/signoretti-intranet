from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import redirect
from . import forms
from . import models

class VendedorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Vendedores
    template_name = 'vendedor_list.html'
    context_object_name = 'vendedores'
    paginate_by = 10
    permission_required = 'crm_vendedores.view_vendedores' 

    def get_queryset(self):
        queryset = super().get_queryset()

        nome = self.request.GET.get('nome', '')
        emitente = self.request.GET.get('emitente', '')
        e_mail = self.request.GET.get('e_mail', '')        
               
        queryset = queryset.filter(status=True)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        
        if emitente:
            queryset = queryset.filter(emitente__cidade__municipio__icontains=emitente)            

        if e_mail:
            queryset = queryset.filter(nome__icontains=e_mail) 
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'nome': self.request.GET.get('nome', ''),
            'emitente': self.request.GET.get('emitente', ''),
            'e_mail': self.request.GET.get('e_mail', ''),
        }      

        context['total_registros'] = self.get_queryset().count()
        
        return context

class VendedorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Vendedores
    template_name = 'vendedor_create.html'
    form_class = forms.VendedorForm
    success_url = reverse_lazy('vendedor_list')
    permission_required = 'crm_vendedores.add_vendedores'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Vendedor cadastrado com sucesso!')
        return response

class VendedorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Vendedores
    template_name = 'vendedor_detail.html' 
    permission_required = 'crm_vendedores.view_vendedores' 
    

class VendedorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Vendedores
    template_name = 'vendedor_update.html'
    form_class = forms.VendedorForm
    success_url = reverse_lazy('vendedor_list')
    permission_required = 'crm_vendedores.change_vendedores' 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Vendedor atualizado com sucesso!')
        return response

class VendedorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Vendedores
    template_name = 'vendedor_delete.html'
    success_url = reverse_lazy('vendedor_list')
    permission_required = 'crm_vendedores.delete_vendedores' 

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object = self.get_object()
        self.object.delete() 
        messages.success(self.request, 'Vendedor inativado com sucesso!')
        return redirect(success_url)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Vendedor inativado com sucesso!')
        return response