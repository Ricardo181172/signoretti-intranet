from django.urls import path
from . import views

urlpatterns = [
    path('ordens_servico/', views.OrdemServicoCreateListView.as_view(), name='ordens_servico_list'),
    path('ordens_servico/<str:pk>/', views.OrdemServicoRetrieveUpdateDestroyView.as_view(), name='ordens_servico-detail-view'),
]
