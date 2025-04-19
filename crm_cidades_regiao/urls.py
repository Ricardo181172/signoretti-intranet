from django.urls import path
from . import views


urlpatterns = [
    path('cidades_regiao/list/', views.CidadeRegiaoListView.as_view(), name='cidade_regiao_list'),
    path('cidades_regiao/create/', views.CidadeRegiaoCreateView.as_view(), name='cidade_regiao_create'),
    path('cidades_regiao/<int:pk>/detail/', views.CidadeRegiaoDetailView.as_view(), name='cidade_regiao_detail'),
    path('cidades_regiao/<int:pk>/update/', views.CidadeRegiaoUpdateView.as_view(), name='cidade_regiao_update'),
    path('cidades_regiao/<int:pk>/delete/', views.CidadeRegiaoDeleteView.as_view(), name='cidade_regiao_delete'),
    path('cidades_regiao/get-cidades/<str:uf>/', views.get_cidades, name='get_cidades'),
]
