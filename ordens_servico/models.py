from django.db import models

class OrdemServico(models.Model):
    os_nr_os = models.CharField(max_length=20, db_column='OS_NrOS', primary_key=True)
    emp_cod_filial = models.CharField(max_length=20, db_column='EMP_CodFilial')
    emp_cnpj = models.CharField(max_length=14, db_column='EMP_CNPJ')
    emp_nome = models.CharField(max_length=210, db_column='EMP_Nome')
    emp_cidade = models.CharField(max_length=600, db_column='EMP_Cidade')
    emp_uf = models.CharField(max_length=2, db_column='EMP_UF')
    os_id_os = models.IntegerField(db_column='OS_IdOS')   
    os_id_cliente = models.IntegerField(db_column='OS_IdCliente')
    os_id_equipamento = models.IntegerField(blank=True, null=True, db_column='OS_IdEquipamento')
    os_dt_avaria = models.DateTimeField(blank=True, null=True, db_column='OS_dtAvaria')
    os_id_situacao_os = models.IntegerField(blank=True, null=True, db_column='OS_IdSituacaoOS')
    sit_cod_situacao_os = models.CharField(max_length=20, blank=True, null=True, db_column='SIT_CodSituacaoOS')
    sit_dsc_situacao_os = models.CharField(max_length=100, blank=True, null=True, db_column='SIT_DscSituacaoOS')
    os_dsc_problema = models.TextField(db_column='OS_DscProblema')
    os_dth_abertura = models.DateTimeField(db_column='OS_DthAbertura')
    os_fstatus = models.CharField(max_length=10, db_column='OS_FStatus')
    os_nr_os_geradora = models.CharField(max_length=20, blank=True, null=True, db_column='OS_NrOSGeradora')
    os_tempo_estimado = models.FloatField(blank=True, null=True, db_column='OS_TempoEstimado')
    os_id_area_operacao = models.IntegerField(blank=True, null=True, db_column='OS_IdAreaOperacao')
    are_cod_area_operacao = models.CharField(max_length=20, blank=True, null=True, db_column='ARE_CodAreaOperacao')
    os_id_tipo_os = models.IntegerField(blank=True, null=True, db_column='OS_IdTipoOS')
    tos_cod_tipo_os = models.CharField(blank=True, null=True, max_length=20, db_column='TOS_CodTipoOS')
    os_dth_previsao_atendimento = models.DateTimeField(blank=True, null=True, db_column='OS_DthPrevisaoAtendimento')
    os_contato_cliente = models.CharField(blank=True, null=True, max_length=100, db_column='OS_ContatoCliente')
    os_contato_telefone = models.CharField(blank=True, null=True, max_length=20, db_column='OS_ContatoTelefone')
    cli_id_empresa = models.IntegerField(db_column='CLI_IdEmpresa')  
    cli_nome = models.CharField(max_length=600, db_column='CLI_Nome')
    cli_codigo_cliente = models.CharField(max_length=20, blank=True, null=True, db_column='CLI_CodigoCliente')
    cli_cnpj_cpf = models.CharField(max_length=20, db_column='CLI_CNPJ_CPF')
    dth_registro = models.DateTimeField(db_column='dthRegistro')

    class Meta:
        db_table = 'cd_matra_ordens_servico'
        ordering = ['os_dth_abertura']                    

    def __str__(self):
        return f'{self.os_nr_os}'
