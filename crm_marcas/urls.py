from django.urls import path
from . import views

urlpatterns = [
    path('marcas/list/', views.MarcaListView.as_view(), name='marca_list'),
    path('marcas/create/', views.MarcaCreateView.as_view(), name='marca_create'),
    path('marcas/<int:pk>/detail/', views.MarcaDetailView.as_view(), name='marca_detail'),
    path('marcas/<int:pk>/update/', views.MarcaUpdateView.as_view(), name='marca_update'),
    path('marcas/<int:pk>/delete/', views.MarcaDeleteView.as_view(), name='marca_delete'),
]
