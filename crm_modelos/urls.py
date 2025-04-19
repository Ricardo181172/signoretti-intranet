from django.urls import path
from . import views


urlpatterns = [
    path('modelos/list/', views.ModeloListView.as_view(), name='modelo_list'),
    path('modelos/create/', views.ModeloCreateView.as_view(), name='modelo_create'),
    path('modelos/<int:pk>/detail/', views.ModeloDetailView.as_view(), name='modelo_detail'),
    path('modelos/<int:pk>/update/', views.ModeloUpdateView.as_view(), name='modelo_update'),
    path('modelos/<int:pk>/delete/', views.ModeloDeleteView.as_view(), name='modelo_delete'),
]