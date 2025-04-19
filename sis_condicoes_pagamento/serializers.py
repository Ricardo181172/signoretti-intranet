from rest_framework import serializers
from .models import CondicoesPagamento


class  CondicoesPagamentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  CondicoesPagamento
        fields = ['descricao',
                  'data_criacao', 
                  'data_ultima_edicao']