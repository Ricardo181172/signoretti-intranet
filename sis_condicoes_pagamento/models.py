from django.db import models


class CondicoesPagamento(models.Model):
    descricao = models.CharField(max_length=50)
    status = models.BooleanField(default=True) 
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'sis_condicoes_pagamento'
        ordering = ['descricao']                    

    def __str__(self):
        return f'{self.descricao}'
