from django.urls import path
from . import views

urlpatterns = [
    path('acessorios_veiculo/list/', views.AcessorioVeiculoListView.as_view(), name='acessorio_veiculo_list'),
    path('acessorios_veiculo/create/', views.AcessorioVeiculoCreateView.as_view(), name='acessorio_veiculo_create'),
    path('acessorios_veiculo/<int:pk>/detail/', views.AcessorioVeiculoDetailView.as_view(), name='acessorio_veiculo_detail'),
    path('acessorios_veiculo/<int:pk>/update/', views.AcessorioVeiculoUpdateView.as_view(), name='acessorio_veiculo_update'),
    path('acessorios_veiculo/<int:pk>/delete/', views.AcessorioVeiculoDeleteView.as_view(), name='acessorio_veiculo_delete'),
]
