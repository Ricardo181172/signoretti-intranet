from django.db import models
from ordens_servico.models import OrdemServico

class AtendimentoOS(models.Model):
    atd_id_atendimento = models.IntegerField(db_column='ATD_IdAtendimento', primary_key=True)
    os_nr_os = models.ForeignKey(
        OrdemServico,
        on_delete=models.CASCADE,
        related_name='ordens_servico_atendimento',
        db_column='OS_NrOS'
    )
    emp_cod_filial = models.CharField(max_length=20, blank=True, null=True, db_column='EMP_CodFilial')
    emp_cnpj = models.CharField(max_length=14, blank=True, null=True, db_column='EMP_CNPJ')
    emp_nome = models.CharField(max_length=200, blank=True, null=True, db_column='EMP_Nome')
    emp_cidade = models.CharField(max_length=600, blank=True, null=True, db_column='EMP_Cidade')
    emp_uf = models.CharField(max_length=2, blank=True, null=True, db_column='EMP_UF')
    os_id_os = models.IntegerField(db_column='OS_IdOS')   
    os_fstatus = models.IntegerField(blank=True, null=True, db_column='OS_FStatus')
    os_id_cliente = models.IntegerField(blank=True, null=True, db_column='OS_IdCliente')
    cli_codigo_cliente = models.CharField(max_length=20, blank=True, null=True, db_column='CLI_CodigoCliente')
    cli_nome = models.CharField(max_length=600, blank=True, null=True, db_column='CLI_Nome')
    cli_cnpj_cpf = models.CharField(max_length=20, blank=True, null=True, db_column='CLI_CNPJ_CPF')    
    usr_cod_usuario = models.CharField(max_length=50, blank=True, null=True, db_column='USR_CodUsuario')
    usr_nome_usuario = models.CharField(max_length=200, blank=True, null=True, db_column='USR_NomeUsuario')
    atd_dsc_causa = models.TextField(blank=True, null=True, db_column='ATD_DscCausa')
    atd_part_number_causadora = models.TextField(blank=True, null=True, db_column='ATD_partNumberCausadora')
    atd_dsc_solucao = models.TextField(blank=True, null=True, db_column='ATD_DscSolucao')
    atd_contado_cliente = models.CharField(max_length=100, blank=True, null=True, db_column='ATD_ContadoCliente')
    atd_contato_telefone = models.CharField(max_length=20, blank=True, null=True, db_column='ATD_ContatoTelefone')
    atd_dth_registro = models.DateTimeField(blank=True, null=True, db_column='ATD_DthRegistro')
    atd_fstatus = models.IntegerField(blank=True, null=True, db_column='ATD_FStatus')
    atd_ano = models.IntegerField(blank=True, null=True, db_column='ATD_Ano')
    atd_mes = models.IntegerField(blank=True, null=True, db_column='ATD_Mes')
    atd_horimetro = models.IntegerField(blank=True, null=True, db_column='ATD_Horimetro')
    atd_dsc_opcional = models.TextField(blank=True, null=True, db_column='ATD_DscOpcional')
    atd_duracao_atendimento = models.FloatField(blank=True, null=True, db_column='ATD_DuracaoAtendimento')
    atd_dth_primeiro_ocorrencia = models.DateTimeField(blank=True, null=True, db_column='ATD_DthPrimeiroOcorrencia')
    atd_dth_ultima_ocorrencia = models.DateTimeField(blank=True, null=True, db_column='ATD_DthUltimaOcorrencia')
    dth_registro = models.DateTimeField(blank=True, null=True, db_column='dthRegistro')

    class Meta:
        db_table = 'cd_matra_atendimentos_os'
        ordering = ['atd_dth_primeiro_ocorrencia']

    def __str__(self):
        return f'OS {self.os_nr_os} - {self.cli_nome}'
