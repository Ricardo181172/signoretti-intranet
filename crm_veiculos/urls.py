from django.urls import path
from . import views

urlpatterns = [
    path('veiculos/list/', views.VeiculoListView.as_view(), name='veiculo_list'),
    path('veiculos/create/', views.VeiculoCreateView.as_view(), name='veiculo_create'),
    path('veiculos/<int:pk>/detail/', views.VeiculoDetailView.as_view(), name='veiculo_detail'),
    path('veiculos/<int:pk>/update/', views.VeiculoUpdateView.as_view(), name='veiculo_update'),
    path('veiculos/<int:pk>/delete/', views.VeiculoDeleteView.as_view(), name='veiculo_delete'),
     path('veiculos/search_modelos/', views.search_modelos, name='search_modelos'),
]
