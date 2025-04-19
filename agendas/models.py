from django.db import models
from ordens_servico.models import OrdemServico

class Agenda(models.Model):
    age_id_agenda = models.IntegerField(db_column='AGE_IdAgenda', primary_key=True)
    os_nr_os = models.ForeignKey(
            OrdemServico,
            on_delete=models.CASCADE,
            db_column='OS_NrOS')
    emp_cod_filial = models.CharField(max_length=10, db_column='EMP_CodFilial')
    emp_id_empresa = models.IntegerField(db_column='EMP_IdEmpresa')    
    os_id_os = models.IntegerField(db_column='OS_IdOS')
    os_fstatus = models.CharField(max_length=9, db_column='OS_FStatus')
    os_id_cliente = models.IntegerField(db_column='OS_IdCliente')
    cli_codigo_cliente = models.CharField(max_length=20, blank=True, null=True, db_column='CLI_CodigoCliente')
    cli_nome = models.CharField(max_length=600, db_column='CLI_Nome')
    cli_cnpj_cpf = models.CharField(max_length=18, db_column='CLI_CNPJ_CPF')
    atd_id_atendimento = models.IntegerField(db_column='ATD_IdAtendimento')
    usr_id_usuario = models.IntegerField(db_column='USR_IdUsuario')
    usr_cod_usuario = models.CharField(max_length=20, db_column='USR_CodUsuario')
    usr_nome_usuario = models.CharField(max_length=200, db_column='USR_NomeUsuario')    
    age_fstatus = models.CharField(max_length=12, db_column='AGE_FStatus')
    age_dth_previsao_inicio = models.DateTimeField(db_column='AGE_DthPrevisaoInicio')
    age_dth_previsao_fim = models.DateTimeField(db_column='AGE_DthPrevisaoFim')
    tps_cod_servico_deslocamento = models.CharField(max_length=50, blank=True, null=True, db_column='TPS_CodServicoDeslocamento')
    tps_dsc_tipo_servico_deslocamento = models.CharField(max_length=1000, blank=True, null=True, db_column='TPS_DscTipoServicoDeslocamento')
    tps_cod_servico_atendimento = models.CharField(max_length=50, blank=True, null=True, db_column='TPS_CodServicoAtendimento')
    tps_dsc_tipo_servico_atendimento = models.CharField(max_length=1000, blank=True, null=True,db_column='TPS_DscTipoServicoAtendimento')
    dth_registro = models.DateTimeField(db_column='dthRegistro')

    class Meta:
        db_table = 'cd_matra_agendas'
        ordering = ['age_dth_previsao_inicio']
        
    def __str__(self):
        return f'{self.age_id_agenda}'

