from rest_framework import serializers
from .models import Metas


class  MetasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Metas
        fields = ['mes', 
                  'ano',
                  'valor',
                  'vendedor',
                  'produto',
                  'tipo_meta',                  
                  'data_criacao', 
                  'data_ultima_edicao']
 