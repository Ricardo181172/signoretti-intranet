from django.db import models
from crm_marcas.models import Marcas
from crm_familias_produto.models import FamiliasProduto


class Modelos(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição do Modelo")
    sigla = models.CharField(null=True, max_length=10, verbose_name="Sigla do Modelo")
    cor = models.CharField(null=True, max_length=20, verbose_name="Cor do Modelo")   
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE, null=True, verbose_name="Marca do Modelo")
    familia_produto = models.ForeignKey(FamiliasProduto, on_delete=models.CASCADE, verbose_name="Familia do Produto do Modelo")
    custo_medio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Custo Médio do Modelo")
    venda_media = models.DecimalField(max_digits=10, decimal_places=2,  null=True, blank=True, verbose_name="Venda Média do Modelo")  
    status = models.BooleanField(default=True, verbose_name="Status do Modelo")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(auto_now=True, verbose_name="Data da Ultima Edição") 

    def delete(self, using=None, keep_parents=False):
        self.status = False
        self.save()  

    class Meta:
        db_table = 'crm_modelos'
        ordering = ['descricao']

    def __str__(self):
        return f'{self.descricao}'
