from rest_framework import serializers
from .models import ConfiguracoesVeiculo


class  ConfiguracoesVeiculoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  ConfiguracoesVeiculo
        fields = ['descricao',
                  'modelo',
                  'top_cat',
                  'acessorio',
                  'data_criacao', 
                  'data_ultima_edicao']
