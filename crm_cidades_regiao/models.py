from django.db import models
from sis_cidades.models import Cidades
from crm_regioes.models import Regioes

class CidadesRegiao(models.Model):
    regiao = models.ForeignKey(Regioes, on_delete=models.CASCADE, verbose_name="Região da Cidade")
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, verbose_name="Cidade")    
    status = models.BooleanField(default=True, verbose_name="Status")
    data_criacao = models.DateTimeField(null=True, auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True, verbose_name="Data da Ultima Edição")    

    def delete(self, using=None, keep_parents=False):
        self.status = False
        self.save()   

    class Meta:
        db_table = 'crm_cidades_regiao'
        ordering = ['regiao']

    def __str__(self):
        return f'{self.cidade} - {self.regiao}'