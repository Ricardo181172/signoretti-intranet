from django.urls import path
from . import views

urlpatterns = [
    path('tipos_venda/list/', views.TipoVendaListView.as_view(), name='tipo_venda_list'),
    path('tipos_venda/create/', views.TipoVendaCreateView.as_view(), name='tipo_venda_create'),
    path('tipos_venda/<int:pk>/detail/', views.TipoVendaDetailView.as_view(), name='tipo_venda_detail'),
    path('tipos_venda/<int:pk>/update/', views.TipoVendaUpdateView.as_view(), name='tipo_venda_update'),
    path('tipos_venda/<int:pk>/delete/', views.TipoVendaDeleteView.as_view(), name='tipo_venda_delete'),
]
