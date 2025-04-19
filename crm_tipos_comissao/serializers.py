from rest_framework import serializers
from .models import TiposComissao


class  TiposComissaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  TiposComissao
        fields = ['descricao', 
                  'data_criacao', 
                  'data_ultima_edicao']
