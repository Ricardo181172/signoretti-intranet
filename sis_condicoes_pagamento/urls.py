from django.urls import path
from . import views

urlpatterns = [
    path('condicoes_pagamento/list/', views.CondicaoPagamentoListView.as_view(), name='condicao_pagamento_list'),
    path('condicoes_pagamento/create/', views.CondicaoPagamentoCreateView.as_view(), name='condicao_pagamento_create'),
    path('condicoes_pagamento/<int:pk>/detail/', views.CondicaoPagamentoDetailView.as_view(), name='condicao_pagamento_detail'),
    path('condicoes_pagamento/<int:pk>/update/', views.CondicaoPagamentoUpdateView.as_view(), name='condicao_pagamento_update'),
    path('condicoes_pagamento/<int:pk>/delete/', views.CondicaoPagamentoDeleteView.as_view(), name='condicao_pagamento_delete'),
]
