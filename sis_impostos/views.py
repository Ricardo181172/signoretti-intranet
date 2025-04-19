from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models

class ImpostoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Impostos
    template_name = 'imposto_list.html'
    context_object_name = 'impostos'
    paginate_by = 10
    permission_required = 'crm_impostos.view_impostos'

    def get_queryset(self):
        queryset = super().get_queryset()

        descricao = self.request.GET.get('descricao', '')        
               
        queryset = queryset.filter(status=True)

        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'descricao': self.request.GET.get('descricao', ''),            
        }         
       
        context['total_registros'] = self.get_queryset().count()
        
        return context

class ImpostoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Impostos
    template_name = 'imposto_create.html'
    form_class = forms.ImpostoForm
    success_url = reverse_lazy('imposto_list')
    permission_required = 'crm_impostos.add_impostos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Imposto cadastrado com sucesso!')
        return response

class ImpostoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Impostos
    template_name = 'imposto_detail.html'
    permission_required = 'crm_impostos.view_impostos'

class ImpostoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Impostos
    template_name = 'imposto_update.html'
    form_class = forms.ImpostoForm
    success_url = reverse_lazy('imposto_list')
    permission_required = 'crm_impostos.update_impostos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Imposto atualizado com sucesso!')
        return response

class ImpostoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Impostos
    template_name = 'imposto_delete.html'
    success_url = reverse_lazy('imposto_list')
    permission_required = 'crm_impostos.delete_impostos'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Imposto inativado com sucesso!')
        return response
