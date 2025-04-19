from django.urls import path
from . import views

urlpatterns = [
    path('pedidos_venda/list/', views.PedidoVendaListView.as_view(), name='pedido_venda_list'),
    path('pedidos_venda/create/', views.PedidoVendaCreateView.as_view(), name='pedido_venda_create'),
    path('pedidos_venda/<int:pk>/detail/', views.PedidoVendaDetailView.as_view(), name='pedido_venda_detail'),
    path('pedidos_venda/<int:pk>/update/', views.PedidoVendaUpdateView.as_view(), name='pedido_venda_update'),
    path('pedidos_venda/<int:pk>/delete/', views.PedidoVendaDeleteView.as_view(), name='pedido_venda_delete'),
    path('ajax/get-veiculos/', views.get_veiculos, name='ajax_get_veiculos'),
]
