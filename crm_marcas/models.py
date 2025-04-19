from django.db import models


class Marcas(models.Model):
    descricao = models.CharField(max_length=100)
    sigla = models.CharField(max_length=5, null=True, blank=True)
    status = models.BooleanField(default=True)       
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now=True)      

    class Meta:
        db_table = 'crm_marcas'
        ordering = ['sigla']

    def __str__(self):
        return f'{self.sigla}'
