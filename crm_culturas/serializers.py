from rest_framework import serializers
from .models import Culturas


class  CulturasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Culturas
        fields = ['descricao',
                  'data_criacao', 
                  'data_ultima_edicao']
