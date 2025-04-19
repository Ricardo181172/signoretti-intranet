from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'), 

    path('api/v1/crm/', views.crm_view, name='crm'),

    path('api/v1/login/', auth_views.LoginView.as_view(), name='login'),

    path('api/v1/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('api/v1/', include('agendas.urls')),  

    path('api/v1/', include('atendimentos_os.urls')),

    path('api/v1/', include('authentication.urls')),    

    path('api/v1/', include('ocorrencias.urls')), 

    path('api/v1/', include('ordens_servico.urls')), 

    path('api/v1/', include('tecnicos.urls')),   

    path('api/v1/', include('tempos_tecnico.urls')),

     path('api/v1/', include('crm_acessorios_veiculo.urls')),

    path('api/v1/', include('crm_areas_cultura.urls')),

    path('api/v1/', include('crm_cidades_regiao.urls')),

    path('api/v1/', include('crm_clientes.urls')),

    path('api/v1/', include('crm_configuracoes_veiculo.urls')),

    path('api/v1/', include('crm_culturas.urls')),

    path('api/v1/', include('crm_empresas.urls')),

    path('api/v1/', include('crm_familias_produto.urls')),
    
    path('api/v1/', include('crm_marcas.urls')),

    path('api/v1/', include('crm_metas.urls')),

    path('api/v1/', include('crm_modelos.urls')),

    path('api/v1/', include('crm_produtos.urls')), 

    path('api/v1/', include('crm_pedidos_venda.urls')),    

    path('api/v1/', include('crm_regioes.urls')),

    path('api/v1/', include('crm_tipos_comissao.urls')),

    path('api/v1/', include('crm_tipos_meta.urls')),

    path('api/v1/', include('crm_tipos_venda.urls')),

    path('api/v1/', include('crm_veiculos.urls')),

    path('api/v1/', include('crm_vendas.urls')),

    path('api/v1/', include('crm_vendedores.urls')),

    path('api/v1/', include('sis_condicoes_pagamento.urls')),
   
    path('api/v1/', include('sis_emitentes.urls')),

    path('api/v1/', include('sis_impostos.urls')),

]
