from rest_framework import serializers
from .models import TemposTecnico


class  TemposTecnicoSerializer(serializers.ModelSerializer):
    #os_nr_os = OrdemServicoSerializer()
    
    class Meta:
        model =  TemposTecnico
        fields = ['tmp_id',
                  'emp_cod_filial',                   
                  'usr_nome_usuario', 
                  'tmp_ano', 
                  'tmp_mes', 
                  'tmp_minutos_disponivel'
                ] 