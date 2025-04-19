from django.db import models

class TemposTecnico(models.Model):
    tmp_id = models.CharField(max_length=30, db_column='TMP_Id', primary_key=True)
    emp_cod_empresa = models.CharField(max_length=10, blank=True, null=True, db_column='EMP_CodEmpresa')
    emp_cod_filial = models.CharField(max_length=10, blank=True, null=True, db_column='EMP_CodFilial')
    usr_nome_usuario = models.CharField(max_length=200, blank=True, null=True, db_column='USR_NomeUsuario')
    usr_cod_usuario = models.CharField(max_length=20, blank=True, null=True, db_column='USR_CodUsuario')
    usr_id_usuario = models.IntegerField(db_column='USR_IdUsuario')
    usr_ativo = models.IntegerField(db_column='USR_Ativo')
    usr_cod_area_operacao = models.CharField(max_length=10, blank=True, null=True, db_column='USR_CodAreaOperacao')
    tmp_ano = models.IntegerField(db_column='TMP_Ano')
    tmp_mes = models.IntegerField(db_column='TMP_Mes')
    tmp_minutos_disponivel = models.FloatField(db_column='TMP_MinutosDisponivel')
    dth_registro = models.DateTimeField(db_column='dthRegistro')

    class Meta:
        db_table = 'cd_matra_tempos_tecnico'
        ordering = ['tmp_id']

    def __str__(self):
        return f'{self.usr_nome_usuario} - {self.emp_cod_empresa}'