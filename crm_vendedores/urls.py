from django.urls import path
from . import views

urlpatterns = [
    path('vendedores/list/', views.VendedorListView.as_view(), name='vendedor_list'),
    path('vendedores/create/', views.VendedorCreateView.as_view(), name='vendedor_create'),
    path('vendedores/<int:pk>/detail/', views.VendedorDetailView.as_view(), name='vendedor_detail'),
    path('vendedores/<int:pk>/update/', views.VendedorUpdateView.as_view(), name='vendedor_update'),
    path('vendedores/<int:pk>/delete/', views.VendedorDeleteView.as_view(), name='vendedor_delete'),
]
