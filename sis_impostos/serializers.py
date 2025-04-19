from rest_framework import serializers
from .models import Impostos


class  ImpostosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Impostos
        fields = ['descricao', 
                  'incidencia',
                  'taxa',
                  'data_criacao', 
                  'data_ultima_edicao']
