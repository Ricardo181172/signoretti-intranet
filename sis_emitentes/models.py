from django.db import models
from sis_cidades.models import Cidades

class Emitentes(models.Model):
    codigo = models.IntegerField(verbose_name="Código da Loja")
    nome = models.CharField(blank=True, null=True, max_length=100, verbose_name="Nome da Loja")
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, verbose_name="Cidade da Loja")
    status = models.BooleanField(default=True, verbose_name="Status do Emitente")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(auto_now=True, verbose_name="Data da Ultima Edição") 

    def delete(self, using=None, keep_parents=False):
        self.status = False
        self.save()

    class Meta:
        db_table = 'sis_emitentes'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome}'    
