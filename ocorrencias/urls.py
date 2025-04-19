from django.urls import path, re_path
from . import views


urlpatterns = [
    path('ocorrencias/', views.OcorrenciaCreateListView.as_view(), name='ocorrencias_list'),
    re_path(r'^ocorrencias/(?P<pk>\d+\.\d+)/$', views.OcorrenciaRetrieveUpdateDestroyView.as_view(), name='ocorrencia_float'),
    #path('ocorrencias/(<int:pk>/', views.OcorrenciaRetrieveUpdateDestroyView.as_view(), name='ocorrencias-detail-view'),
    #path('ocorrencias/(?P<value>\d+\.\d+)/$/', views.OcorrenciaRetrieveUpdateDestroyView.as_view(), name='ocorrencias-detail-view'),
]
