from rest_framework import serializers
from .models import Emitentes


class  EmitentesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Emitentes
        fields = ['codigo', 
                  'nome', 
                  'cidade',
                  'data_criacao', 
                  'data_ultima_edicao']
