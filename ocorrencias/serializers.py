from rest_framework import serializers
from ocorrencias.models import Ocorrencia
from ordens_servico.serializers import OrdemServicoSerializer
from .models import Ocorrencia


class  OcorrenciaSerializer(serializers.ModelSerializer):
    #os_nr_os = OrdemServicoSerializer()
    ose_dth_ocorrencia = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    ose_dth_original = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')

    class Meta:
        model =  Ocorrencia
        fields = ['ose_id_osocr', 
                  'emp_cod_filial',                  
                  'os_nr_os',
                  'ose_dth_ocorrencia',
                  'usr_nome_usuario',       
                  'ose_dsc_ocorrencia',                   
                  'ose_observacao', 
                  'ose_latitude', 
                  'ose_longitude', 
                  'os_km', 
                  'ose_dsc_situacao_ocorrencia', 
                  'ose_dth_original', 
                  'ose_dsc_motivo_pausa', 
                  'trf_cod_integracao', 
                  'trf_tempo_estimado', 
                  'trf_dsc_tarefa',                   
                  'trf_preco_tarefa',
                  'trf_quantidade',
                  'trf_status'                              
                  ]
