from django.db import models


class TiposVenda(models.Model):
    descricao = models.CharField(max_length=50)     
    status = models.BooleanField(default=True)      
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now=True)      

    class Meta:
        db_table = 'crm_tipos_venda'
        ordering = ['descricao']

    def __str__(self):
        return f'OS {self.descricao}'
