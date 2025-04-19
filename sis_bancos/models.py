from django.db import models


class Bancos(models.Model):
    num_banco = models.IntegerField()   
    nome = models.TextField(null=True)     

    class Meta:
        db_table = 'sis_bancos'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome}'