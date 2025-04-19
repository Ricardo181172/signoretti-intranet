from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import JsonResponse
from django.shortcuts import redirect
from . import forms
from . import models
from sis_cidades.models import Cidades

class EmitenteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Emitentes
    template_name = 'emitente_list.html'
    context_object_name = 'emitentes'
    paginate_by = 10
    permission_required = 'crm_emitentes.view_emitentes'

    def get_queryset(self):
        queryset = super().get_queryset()

        codigo = self.request.GET.get('codigo', '')
        nome = self.request.GET.get('nome', '')
        cidade = self.request.GET.get('cidade', '')
               
        queryset = queryset.filter(status=True)

        if codigo:
            queryset = queryset.filter(codigo__icontains=codigo)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
       
        if cidade:
         queryset = queryset.filter(cidade__municipio__icontains=cidade)       
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'codigo': self.request.GET.get('codigo', ''),
            'nome': self.request.GET.get('nome', ''),
            'cidade': self.request.GET.get('cidade', ''),            
        }     

        context['total_registros'] = self.get_queryset().count()
        
        return context

class EmitenteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Emitentes
    template_name = 'emitente_create.html'
    form_class = forms.EmitenteForm
    success_url = reverse_lazy('emitente_list')
    permission_required = 'crm_emitentes.add_emitentes'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Emitente cadastrado com sucesso!')
        return response

class EmitenteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Emitentes
    template_name = 'emitente_detail.html'
    permission_required = 'crm_emitentes.view_emitentes'

class EmitenteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Emitentes
    template_name = 'emitente_update.html'
    form_class = forms.EmitenteForm
    success_url = reverse_lazy('emitente_list')
    permission_required = 'crm_emitentes.change_emitentes'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Emitente atualizado com sucesso!')
        return response

class EmitenteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Emitentes
    template_name = 'emitente_delete.html'
    success_url = reverse_lazy('emitente_list')
    permission_required = 'crm_emitentes.delete_emitentes'
    
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object = self.get_object()
        self.object.delete() 
        messages.success(self.request, 'Emitente inativado com sucesso!')
        return redirect(success_url)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Emitente inativado com sucesso!')
        return response

def get_cidades(request, uf):
    cidades = Cidades.objects.filter(uf=uf).values('id', 'municipio')
    return JsonResponse({'cidades': list(cidades)})