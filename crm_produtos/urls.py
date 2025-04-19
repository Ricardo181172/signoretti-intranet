from django.urls import path
from . import views


urlpatterns = [
    path('produtos/list/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/create/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/detail/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/<int:pk>/update/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
]
