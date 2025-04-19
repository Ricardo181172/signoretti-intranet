from rest_framework import serializers
from .models import FamiliasProduto


class  FamiliasProdutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  FamiliasProduto
        fields = ['descricao', 
                  'sigla',
                  'produto',
                  'data_criacao', 
                  'data_ultima_edicao']
