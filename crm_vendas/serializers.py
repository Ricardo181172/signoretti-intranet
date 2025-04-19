from rest_framework import serializers
from .models import CidadesRegiao


class  CidadesRegiaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  CidadesRegiao
        fields = ['regiao', 
                  'cidade',
                  'data_criacao', 
                  'data_ultima_edicao'
                ]
