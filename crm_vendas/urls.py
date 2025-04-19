from django.urls import path
from . import views


urlpatterns = [
    path('vendas/list/', views.VendaListView.as_view(), name='venda_list'),
    path('vendas/create/', views.VendaCreateView.as_view(), name='venda_create'),
    path('vendas/<int:pk>/detail/', views.VendaDetailView.as_view(), name='venda_detail'),
    path('vendas/<int:pk>/update/', views.VendaUpdateView.as_view(), name='venda_update'),
    path('vendas/<int:pk>/delete/', views.VendaDeleteView.as_view(), name='venda_delete'),
]
