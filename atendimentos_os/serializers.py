from rest_framework import serializers
from ordens_servico.models import OrdemServico
from ordens_servico.serializers import OrdemServicoSerializer
from .models import AtendimentoOS


class  AtendimentoOSSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  AtendimentoOS
        fields = ['atd_id_atendimento', 
                  'emp_cod_filial', 
                  'os_nr_os', 
                  'atd_dth_registro', 
                  'cli_nome', 
                  'usr_nome_usuario', 
                  'atd_dsc_causa', 
                  'atd_part_number_causadora', 
                  'atd_dsc_solucao', 
                  'atd_horimetro', 
                  'atd_dsc_opcional', 
                  'atd_duracao_atendimento', 
                  'atd_dth_primeiro_ocorrencia', 
                  'atd_dth_ultima_ocorrencia', 
                  'atd_contado_cliente', 
                  'atd_contato_telefone']
