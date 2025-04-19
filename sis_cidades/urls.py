from django.urls import path
from . import views

urlpatterns = [
    path('sis_cidades/', views.CidadesCreateListView.as_view(), name='sis_cidades-list'),
    path('sis_cidades/<int:pk>/', views.CidadesRetrieveUpdateDestroyView.as_view(), name='sis_cidades-detail-view'),
]