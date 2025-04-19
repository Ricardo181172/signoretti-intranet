from rest_framework import serializers
from .models import OrdemServico

class OrdemServicoSerializer(serializers.ModelSerializer):
    #os_dth_abertura = serializers.DateTimeField(format='%d/%m/%Y')

    class Meta:
        model = OrdemServico
        fields = ['emp_cod_filial', 
                  'os_nr_os', 
                  'os_dth_abertura', 
                  'os_fstatus',
                  'sit_dsc_situacao_os', 
                  'cli_nome', 
                  'tos_cod_tipo_os', 
                  'os_dsc_problema']