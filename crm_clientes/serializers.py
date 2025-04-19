from rest_framework import serializers
from .models import Clientes


class  ClientesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Clientes
        fields = ['emitente',
                  'nome', 
                  'cidade',
                  'vendedor',
                  'categoria',                    
                  'cpf_cnpj',
                  'tipo_cliente',
                  'e_mail',
                  'frota_ativa',
                  'frota_total',
                  'latitude',
                  'longitude',                    
                  'status',
                  'data_criacao', 
                  'data_ultima_edicao']
 