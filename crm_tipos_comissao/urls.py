from django.urls import path
from . import views

urlpatterns = [
    path('tipos_comissao/list/', views.TipoComissaoListView.as_view(), name='tipo_comissao_list'),
    path('tipos_comissao/create/', views.TipoComissaoCreateView.as_view(), name='tipo_comissao_create'),
    path('tipos_comissao/<int:pk>/detail/', views.TipoComissaoDetailView.as_view(), name='tipo_comissao_detail'),
    path('tipos_comissao/<int:pk>/update/', views.TipoComissaoUpdateView.as_view(), name='tipo_comissao_update'),
    path('tipos_comissao/<int:pk>/delete/', views.TipoComissaoDeleteView.as_view(), name='tipo_comissao_delete'),
]
