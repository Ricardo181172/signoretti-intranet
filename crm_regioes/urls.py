from django.urls import path
from . import views

urlpatterns = [
    path('regioes/list/', views.RegiaoListView.as_view(), name='regiao_list'),
    path('regioes/create/', views.RegiaoCreateView.as_view(), name='regiao_create'),
    path('regioes/<int:pk>/detail/', views.RegiaoDetailView.as_view(), name='regiao_detail'),
    path('regioes/<int:pk>/update/', views.RegiaoUpdateView.as_view(), name='regiao_update'),
    path('regioes/<int:pk>/delete/', views.RegiaoDeleteView.as_view(), name='regiao_delete'),
]
