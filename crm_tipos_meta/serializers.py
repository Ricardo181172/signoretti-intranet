from rest_framework import serializers
from .models import TiposVenda


class  TiposVendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  TiposVenda
        fields = ['descricao',                   
                  'data_criacao', 
                  'data_ultima_edicao']
