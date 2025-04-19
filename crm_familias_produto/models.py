from django.db import models
from crm_produtos.models import Produtos


class FamiliasProduto(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição do Modelo")
    sigla = models.CharField(null=True, max_length=10, verbose_name="Sigla do Modelo")
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, verbose_name="Tipo do Equipamento do Modelo")
    status = models.BooleanField(default=True, verbose_name="Status do Modelo")
    data_criacao = models.DateTimeField(null=True, auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True, verbose_name="Data da Ultima Edição")          

    class Meta:
        db_table = 'crm_familias_produto'
        ordering = ['descricao']

    def __str__(self):
        return f'{self.descricao}'
    

    


