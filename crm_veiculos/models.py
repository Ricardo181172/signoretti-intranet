from django.db import models
from sis_emitentes.models import Emitentes
from crm_modelos.models import Modelos
from crm_acessorios_veiculo.models import AcessoriosVeiculo

class Veiculos(models.Model):    
    emitente = models.ForeignKey(Emitentes, on_delete=models.CASCADE)
    estado = models.CharField(blank=True, null=True, max_length=20)
    modelo = models.ForeignKey(Modelos, on_delete=models.CASCADE)
    acessorio_veiculo = models.ForeignKey(AcessoriosVeiculo, blank=True, null=True, on_delete=models.CASCADE)
    prazo_free = models.IntegerField(blank=True, null=True)
    serie = models.CharField(blank=True, null=True, max_length=50)
    chassi = models.CharField(blank=True, null=True, max_length=50, unique=True)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.CharField(blank=True, null=True, max_length=50)
    data_compra = models.DateField(null=True, blank=True)
    data_pedido = models.DateField(null=True, blank=True)
    data_venda = models.DateField(null=True, blank=True)
    data_quitacao = models.DateField(null=True, blank=True)
    nf_compra = models.IntegerField(null=True, blank=True)
    nf_venda = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(null=True, auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True)    

    class Meta:
        db_table = 'crm_veiculos'
        ordering = ['modelo']

    def __str__(self):
        return f'{self.modelo} - {self.chassi}'
