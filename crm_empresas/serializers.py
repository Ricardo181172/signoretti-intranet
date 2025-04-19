from rest_framework import serializers
from .models import Empresas


class  EmpresasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Empresas
        fields = ['nome',                   
                  'cidade',
                  'tipo_empresa',
                  'data_criacao', 
                  'data_ultima_edicao']
