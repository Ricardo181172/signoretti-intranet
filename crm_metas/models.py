from django.db import models
from crm_tipos_meta.models import TiposMeta
from crm_produtos.models import Produtos
from crm_vendedores.models import Vendedores


class Metas(models.Model):
    
    mes = models.IntegerField(
        choices=[(i, f"{i:02}") for i in range(1, 13)],  # Opções de 01 a 12 representando os meses
        verbose_name="Mês"
    )
    ano = models.IntegerField(
        verbose_name="Ano"
    )
    quantidade = models.IntegerField(
        null=True,
        choices=[(i, f"{i:02}") for i in range(1, 20)],  # Opções de 01 a 12 representando os meses
        verbose_name="Quantidade"
    )
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Meta de Vendas"
    ) 
    vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)  
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)     
    tipo_meta = models.ForeignKey(TiposMeta, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)     
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now=True)      

    class Meta:
        db_table = 'crm_metas'
        ordering = ['tipo_meta']

    def __str__(self):
        return f'{self.mes} - {self.ano} - {self.produto} - {self.vendedor}'
