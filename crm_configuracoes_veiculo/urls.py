from django.urls import path
from . import views

urlpatterns = [
    path('configuracoes_veiculo/list/', views.ConfiguracaoVeiculoListView.as_view(), name='configuracao_veiculo_list'),
    path('configuracoes_veiculo/create/', views.ConfiguracaoVeiculoCreateView.as_view(), name='configuracao_veiculo_create'),
    path('configuracoes_veiculo/<int:pk>/detail/', views.ConfiguracaoVeiculoDetailView.as_view(), name='configuracao_veiculo_detail'),
    path('configuracoes_veiculo/<int:pk>/update/', views.ConfiguracaoVeiculoUpdateView.as_view(), name='configuracao_veiculo_update'),
    path('configuracoes_veiculo/<int:pk>/delete/', views.ConfiguracaoVeiculoDeleteView.as_view(), name='configuracao_veiculo_delete'),
]
