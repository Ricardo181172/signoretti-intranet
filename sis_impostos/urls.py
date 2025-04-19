from django.urls import path
from . import views

urlpatterns = [
    path('impostos/list/', views.ImpostoListView.as_view(), name='imposto_list'),
    path('impostos/create/', views.ImpostoCreateView.as_view(), name='imposto_create'),
    path('impostos/<int:pk>/detail/', views.ImpostoDetailView.as_view(), name='imposto_detail'),
    path('impostos/<int:pk>/update/', views.ImpostoUpdateView.as_view(), name='imposto_update'),
    path('impostos/<int:pk>/delete/', views.ImpostoDeleteView.as_view(), name='imposto_delete'),
]
