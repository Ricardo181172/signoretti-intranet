from rest_framework import serializers
from .models import Produtos


class  ProdutosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Produtos
        fields = ['descricao', 
                  'sigla',
                  'data_criacao', 
                  'data_ultima_edicao']
