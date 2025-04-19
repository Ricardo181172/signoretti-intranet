from rest_framework import serializers
from .models import Marcas


class  MarcasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Marcas
        fields = ['descricao',
                  'sigla',
                  'data_criacao', 
                  'data_ultima_edicao']
