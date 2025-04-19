from django.urls import path
from . import views

urlpatterns = [
    path('tempos_tecnico/', views.TemposTecnicoCreateListView.as_view(), name='tempos_tecnico_list'),
    path('tempos_tecnico/<str:pk>/', views.TemposTecnicoRetrieveUpdateDestroyView.as_view(), name='tempos_tecnico-detail-view'),
]
