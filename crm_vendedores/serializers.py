from rest_framework import serializers
from .models import Vendedores


class  VendedoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Vendedores
        fields = ['nome', 
                  'sobrenome', 
                  'emitente',
                  'e_mail', 
                  'celular', 
                  'usuario_crm',
                  'senha_crm', 
                  'data_criacao', 
                  'data_ultima_edicao']
