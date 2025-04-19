from rest_framework import serializers
from .models import Veiculos


class  VeiculosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Veiculos
        fields = ['emitente',
                  'estado',
                  'modelo', 
                  'acessorio_veiculo', 
                  'prazo_free',                      
                  'serie',                      
                  'chassi',
                  'valor_custo',
                  'valor_venda', 
                  'situacao', 
                  'data_compra',                       
                  'data_pedido',                      
                  'data_venda',
                  'data_quitacao',
                  'nf_compra',
                  'nf_venda',
                  'data_criacao', 
                  'data_ultima_edicao']
 