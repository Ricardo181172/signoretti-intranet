from rest_framework import serializers
from .models import AreasCultura


class  AreasCulturaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  AreasCultura
        fields = ['ano', 
                  'regiao',
                  'cultura',
                  'data_criacao', 
                  'data_ultima_edicao'
                ]
