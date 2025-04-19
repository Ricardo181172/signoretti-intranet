from django.db import models
from sis_emitentes.models import Emitentes
from crm_vendedores.models import Vendedores
from crm_veiculos.models import Veiculos
from crm_clientes.models import Clientes
from sis_bancos.models import Bancos

class PedidosVenda(models.Model):

    emitente = models.ForeignKey(Emitentes, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculos, on_delete=models.CASCADE)    
    vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    status_negociacao = models.CharField(null=True, max_length=50)
    status_financiamento = models.CharField(null=True, max_length=50)
    banco = models.ForeignKey(Bancos, default=0, on_delete=models.CASCADE)   
    valor = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    outras_receitas = models.DecimalField(max_digits=10, default=0, decimal_places=2) 
    outras_despesas = models.DecimalField(max_digits=10, default=0, decimal_places=2) 
    linha_credito = models.CharField(null=True, max_length=50) 
    taxa_flat = models.DecimalField(max_digits=5, decimal_places=2, null=True) 
    porcent_financiamento = models.IntegerField(null=True, blank=True)
    data_pedido = models.DateField(null=True, blank=True) 
    data_envio_proposta = models.DateField(null=True, blank=True)
    data_aprovacao = models.DateField(null=True, blank=True)
    data_recebimento = models.DateField(null=True, blank=True)
    situacao_financiamento = models.TextField(null=True, blank=True)
    observacoes = models.TextField(null=True)  
    status = models.BooleanField(default=True)   
    data_criacao = models.DateTimeField(null=True, auto_now_add=True)    
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True)      

    class Meta:
        db_table = 'crm_pedidos_venda'
        ordering = ['cliente']

    def __str__(self):
        return f'{self.cliente} - {self.veiculo}'
