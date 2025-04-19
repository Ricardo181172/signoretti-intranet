from django.db import models
from crm_regioes.models import Regioes
from crm_culturas.models import Culturas

class AreasCultura(models.Model):
    ano = models.IntegerField(verbose_name="Ano")    
    regiao = models.ForeignKey(Regioes, on_delete=models.CASCADE, verbose_name="Região")
    cultura = models.ForeignKey(Culturas, on_delete=models.CASCADE, verbose_name="Cidade")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Área em Hectares")
    status = models.BooleanField(default=True, verbose_name="Status")
    data_criacao = models.DateTimeField(null=True, auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True, verbose_name="Data da Ultima Edição") 
    class Meta:
        db_table = 'crm_areas_cultura'
        ordering = ['regiao']

    def __str__(self):
        return f'{self.regiao} - {self.cultura}'