from django.urls import path
from . import views

urlpatterns = [
    path('culturas/list/', views.CulturaListView.as_view(), name='cultura_list'),
    path('culturas/create/', views.CulturaCreateView.as_view(), name='cultura_create'),
    path('culturas/<int:pk>/detail/', views.CulturaDetailView.as_view(), name='cultura_detail'),
    path('culturas/<int:pk>/update/', views.CulturaUpdateView.as_view(), name='cultura_update'),
    path('culturas/<int:pk>/delete/', views.CulturaDeleteView.as_view(), name='cultura_delete'),
]
