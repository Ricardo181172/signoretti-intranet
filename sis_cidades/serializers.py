from rest_framework import serializers
from .models import Cidades


class  CidadesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Cidades
        fields = ['uf', 
                  'municipio', 
                  'regiao', 
                  'populacao',
                  'porte']