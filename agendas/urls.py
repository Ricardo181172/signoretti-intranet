from django.urls import path
from . import views

urlpatterns = [
    path('agendas/list/', views.AgendaListView.as_view(), name='agendas_list'),
    path('agendas/', views.AgendaCreateListView.as_view(), name='agendas_lists'),
    #path('agendas/<int:pk>/', views.AgendaRetrieveUpdateDestroyView.as_view(), name='agenda-detail-view'),
]
