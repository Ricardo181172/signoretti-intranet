from django.db import models
from ordens_servico.models import OrdemServico


class Ocorrencia(models.Model):
    ose_id_osocr = models.FloatField(db_column='OSE_IdOSOCr', primary_key=True)
    os_nr_os = models.ForeignKey(
        OrdemServico,
        on_delete=models.CASCADE,        
        related_name='ordens_servico_ocorrencia',
        db_column='OS_NrOS'
    )
    ose_id_os = models.FloatField(db_column='OSE_IdOS')   
    ose_id_ocorrencia = models.FloatField(db_column='OSE_IdOcorrencia')
    ose_dsc_ocorrencia = models.CharField(max_length=100, db_column='OSE_DscOcorrencia')
    ose_id_usuario = models.FloatField(db_column='OSE_IdUsuario')
    ose_dth_ocorrencia = models.DateTimeField(db_column='OSE_DthOcorrencia')
    ose_observacao = models.TextField(blank=True, null=True, db_column='OSE_Observacao')
    ose_latitude = models.FloatField(blank=True, null=True, db_column='OSE_Latitude')
    ose_longitude = models.FloatField(blank=True, null=True, db_column='OSE_Longitude')
    os_km = models.IntegerField(blank=True, null=True, db_column='OS_KM')
    ose_id_agenda = models.FloatField(db_column='OSE_IdAgenda')
    ose_id_situacao_ocorrencia = models.FloatField(blank=True, null=True, db_column='OSE_IdSituacaoOcorrencia')
    ose_dsc_situacao_ocorrencia = models.CharField(max_length=50, db_column='OSE_DscSituacaoOcorrencia')
    ose_id_tipo_origem = models.IntegerField(db_column='OSE_IdTipoOrigem')
    ose_dth_original = models.DateTimeField(blank=True, null=True, db_column='OSE_DthOriginal')
    ose_id_motivo_pausa = models.FloatField(blank=True, null=True, db_column='OSE_IdMotivoPausa')
    ose_dsc_motivo_pausa = models.CharField(max_length=200, blank=True, null=True, db_column='OSE_DscMotivoPausa')
    trf_cod_integracao = models.CharField(max_length=200, blank=True, null=True, db_column='TRF_CodIntegracao')
    trf_tempo_estimado = models.FloatField(blank=True, null=True, db_column='TRF_TempoEstimado')
    trf_dsc_tarefa = models.CharField(max_length=200, blank=True, null=True, db_column='TRF_DscTarefa')
    trf_preco_tarefa = models.FloatField(blank=True, null=True, db_column='TRF_PrecoTarefa')
    trf_quantidade = models.FloatField(blank=True, null=True, db_column='TRF_Quantidade')
    trf_status = models.CharField(blank=True, null=True, max_length=20, db_column='TRF_Status')
    usr_nome_usuario = models.CharField(max_length=200, db_column='USR_NomeUsuario')
    usr_cod_usuario = models.CharField(max_length=20, db_column='USR_CodUsuario')
    emp_cod_filial = models.CharField(max_length=10, db_column='EMP_CodFilial')
    dth_registro = models.DateTimeField(db_column='dthRegistro')
    
    class Meta:
        db_table = 'cd_matra_ocorrencias'
        ordering = ['ose_dth_original']
        
    def __str__(self):
        return f'Ocorrência {self.ose_id_ocorrencia} - {self.os_nr_os}'
