from django.urls import path
from . import views

urlpatterns = [
    path('tipos_meta/list/', views.TipoMetaListView.as_view(), name='tipo_meta_list'),
    path('tipos_meta/create/', views.TipoMetaCreateView.as_view(), name='tipo_meta_create'),
    path('tipos_meta/<int:pk>/detail/', views.TipoMetaDetailView.as_view(), name='tipo_meta_detail'),
    path('tipos_meta/<int:pk>/update/', views.TipoMetaUpdateView.as_view(), name='tipo_meta_update'),
    path('tipos_meta/<int:pk>/delete/', views.TipoMetaDeleteView.as_view(), name='tipo_meta_delete'),
]
