from rest_framework import serializers
from .models import Regioes


class  RegioesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Regioes
        fields = ['descricao', 
                  'data_criacao', 
                  'data_ultima_edicao']
