from django.urls import path
from . import views


urlpatterns = [
    path('areas_cultura/list/', views.AreaCulturaListView.as_view(), name='area_cultura_list'),
    path('areas_cultura/create/', views.AreaCulturaCreateView.as_view(), name='area_cultura_create'),
    path('areas_cultura/<int:pk>/detail/', views.AreaCulturaDetailView.as_view(), name='area_cultura_detail'),
    path('areas_cultura/<int:pk>/update/', views.AreaCulturaUpdateView.as_view(), name='area_cultura_update'),
    path('areas_cultura/<int:pk>/delete/', views.AreaCulturaDeleteView.as_view(), name='area_cultura_delete'),
]
