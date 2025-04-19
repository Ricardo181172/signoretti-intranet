
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models


class AreaCulturaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.AreasCultura
    template_name = 'area_cultura_list.html'
    context_object_name = 'areas_cultura'
    paginate_by = 10
    permission_required = 'crm_areas_cultura.view_areascultura'

    def get_queryset(self):
        queryset = super().get_queryset()

        ano = self.request.GET.get('ano', '')
        regiao = self.request.GET.get('regiao', '')
        cultura = self.request.GET.get('cultura', '')
               
        queryset = queryset.filter(status=True)

        if ano:
            queryset = queryset.filter(ano__icontains=ano)

        if regiao:
            queryset = queryset.filter(regiao__descricao__icontains=regiao)
       
        if cultura:
         queryset = queryset.filter(cultura__descricao__icontains=cultura)       
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os valores dos filtros ao contexto
        context['filtros'] = {
            'ano': self.request.GET.get('ano', ''),
            'regiao': self.request.GET.get('regiao', ''),
            'cultura': self.request.GET.get('cultura', ''),            
        }     

        context['total_registros'] = self.get_queryset().count()
        
        return context

class AreaCulturaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.AreasCultura
    template_name = 'area_cultura_create.html'
    form_class = forms.AreaCulturaForm
    success_url = reverse_lazy('area_cultura_list')
    permission_required = 'crm_areas_cultura.add_areascultura'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente cadastrado com sucesso!')
        return response

class AreaCulturaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.AreasCultura
    template_name = 'area_cultura_detail.html'
    permission_required = 'crm_areas_cultura.view_areascultura'

class AreaCulturaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.AreasCultura
    template_name = 'area_cultura_update.html'
    form_class = forms.AreaCulturaForm
    success_url = reverse_lazy('area_cultura_list')
    permission_required = 'crm_areas_cultura.change_areascultura'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar o cliente. Por favor, verifique os campos.')
        return super().form_invalid(form)

class AreaCulturaDeleteView(LoginRequiredMixin, DeleteView):
    model = models.AreasCultura
    template_name = 'area_cultura_delete.html'
    success_url = reverse_lazy('area_cultura_list')
    permission_required = 'crm_areas_cultura.delete_areascultura'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Cliente inativado com sucesso!')
        return response
    