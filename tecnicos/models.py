from django.db import models

class Tecnico(models.Model):
    usr_cod_usuario = models.CharField(max_length=30, db_column='USR_CodUsuario', primary_key=True)
    usr_id_usuario = models.IntegerField(db_column='USR_IdUsuario')
    usr_cpf = models.CharField(max_length=14, db_column='USR_CPF') 
    usr_nome_usuario = models.CharField(max_length=200, db_column='USR_NomeUsuario')
    usr_login = models.CharField(max_length=200,db_column='USR_Login')
    usr_tipo_usuario = models.CharField(max_length=1, db_column='USR_TipoUsuario')
    usr_dsc_tipo_usuario = models.CharField(max_length=20, db_column='USR_DscTipoUsuario')
    usr_id_empresa = models.IntegerField(db_column='USR_IdEmpresa')
    usr_email = models.EmailField(max_length=255, blank=True, null=True, db_column='USR_Email')
    usr_id_licenca = models.CharField(max_length=50, blank=True, null=True, db_column='USR_IdLicenca')
    usr_dth_registro = models.DateTimeField(db_column='USR_DthRegistro')    
    emp_id_empresa = models.IntegerField(db_column='EMP_IdEmpresa')
    emp_nome = models.CharField(max_length=200, db_column='EMP_Nome')
    emp_cidade = models.CharField(max_length=100, db_column='EMP_Cidade')
    emp_cod_filial = models.CharField(max_length=10, db_column='EMP_CodFilial')
    dth_registro = models.DateTimeField(db_column='dthRegistro')

    class Meta:
        db_table = 'cd_matra_tecnicos'
        ordering = ['usr_nome_usuario']

    def __str__(self):
        return f'{self.usr_nome_usuario} ({self.emp_nome})'
