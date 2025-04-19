from django.urls import path
from . import views

urlpatterns = [
    path('atendimentos_os/', views.AtendimentoOSCreateListView.as_view(), name='atendimentos_os-list'),
    path('atendimentos_os/<int:pk>/', views.AtendimentoOSRetrieveUpdateDestroyView.as_view(), name='atendimentos_os-detail-view'),
    path('atendimentos_os/stats/', views.AtendimentoOSStatsView.as_view(), name='atendimentos_os-stats-view'),
]
