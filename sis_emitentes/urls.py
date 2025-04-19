from django.urls import path
from . import views

urlpatterns = [
    path('emitentes/list/', views.EmitenteListView.as_view(), name='emitente_list'),
    path('emitentes/create/', views.EmitenteCreateView.as_view(), name='emitente_create'),
    path('emitentes/<int:pk>/detail/', views.EmitenteDetailView.as_view(), name='emitente_detail'),
    path('emitentes/<int:pk>/update/', views.EmitenteUpdateView.as_view(), name='emitente_update'),
    path('emitentes/<int:pk>/delete/', views.EmitenteDeleteView.as_view(), name='emitente_delete'),
    path('emitentes/get-cidades/<str:uf>/', views.get_cidades, name='get_cidades'),
]
