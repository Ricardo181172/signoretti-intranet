# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import metricas

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'home.html', context)  # Vamos criar este template

@login_required(login_url='login')
def crm_view(request):
    metricas_veiculos = metricas.get_metricas_veiculos()
    metricas_pedidos_venda = metricas.get_metricas_pedidos_venda()
   
    context = {
        'metricas_veiculos': metricas_veiculos,
        'metricas_pedidos_venda': metricas_pedidos_venda
    }
    return render(request, 'crm.html', context)