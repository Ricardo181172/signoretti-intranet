from rest_framework import serializers
from .models import AcessoriosVeiculo


class  AcessoriosVeiculoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  AcessoriosVeiculo
        fields = ['descricao',
                  'data_criacao', 
                  'data_ultima_edicao']
