from django.db import models


class TiposMeta(models.Model):
    descricao = models.CharField(max_length=50)    
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True) 
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now=True)       

    class Meta:
        db_table = 'crm_tipos_meta'
        ordering = ['descricao']

    def __str__(self):
        return f'{self.descricao}'
