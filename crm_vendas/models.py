from django.db import models
from crm_pedidos_venda.models import PedidosVenda

class Vendas(models.Model):    
    pedido_venda = models.ForeignKey(PedidosVenda, on_delete=models.CASCADE)   
    nf_venda = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(null=True, auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True)    

    class Meta:
        db_table = 'crm_vendas'
        ordering = ['pedido_venda']

    def __str__(self):
        return f'{self.pedido_venda}'
