from rest_framework import serializers
from ordens_servico.models import OrdemServico
from ordens_servico.serializers import OrdemServicoSerializer
from .models import Agenda


class  AgendaSerializer(serializers.ModelSerializer):
    #os_nr_os = OrdemServicoSerializer()

    class Meta:
        model =  Agenda
        fields = ['age_id_agenda', 'emp_cod_filial', 'os_nr_os', 'os_fstatus', 'cli_nome', 'age_dth_previsao_inicio', 'age_dth_previsao_fim', 'usr_nome_usuario']
