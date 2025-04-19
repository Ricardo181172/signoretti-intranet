from django.urls import path
from . import views

urlpatterns = [
    path('metas/list/', views.MetaListView.as_view(), name='meta_list'),
    path('metas/create/', views.MetaCreateView.as_view(), name='meta_create'),
    path('metas/<int:pk>/detail/', views.MetaDetailView.as_view(), name='meta_detail'),
    path('metas/<int:pk>/update/', views.MetaUpdateView.as_view(), name='meta_update'),
    path('metas/<int:pk>/delete/', views.MetaDeleteView.as_view(), name='meta_delete'),
]
