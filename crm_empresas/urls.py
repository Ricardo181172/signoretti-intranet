from django.urls import path
from . import views


urlpatterns = [
    path('empresas/list/', views.EmpresaListView.as_view(), name='empresa_list'),
    path('empresas/create/', views.EmpresaCreateView.as_view(), name='empresa_create'),
    path('empresas/<int:pk>/detail/', views.EmpresaDetailView.as_view(), name='empresa_detail'),
    path('empresas/<int:pk>/update/', views.EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresas/<int:pk>/delete/', views.EmpresaDeleteView.as_view(), name='empresa_delete'),
    path('empresas/get-cidades/<str:uf>/', views.get_cidades, name='get_cidades'),
]
