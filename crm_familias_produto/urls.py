from django.urls import path
from . import views


urlpatterns = [
    path('familias_produto/list/', views.FamiliaProdutoListView.as_view(), name='familia_produto_list'),
    path('familias_produto/create/', views.FamiliaProdutoCreateView.as_view(), name='familia_produto_create'),
    path('familias_produto/<int:pk>/detail/', views.FamiliaProdutoDetailView.as_view(), name='familia_produto_detail'),
    path('familias_produto/<int:pk>/update/', views.FamiliaProdutoUpdateView.as_view(), name='familia_produto_update'),
    path('familias_produto/<int:pk>/delete/', views.FamiliaProdutoDeleteView.as_view(), name='familia_produto_delete'),
]
