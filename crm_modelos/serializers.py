from rest_framework import serializers
from .models import Series


class  SeriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Series
        fields = ['descricao', 
                  'sigla',
                  'cor',                
                  'familia_produto',
                  'marca',
                  'custo_medio',
                  'venda_media',
                  'data_criacao', 
                  'data_ultima_edicao']
