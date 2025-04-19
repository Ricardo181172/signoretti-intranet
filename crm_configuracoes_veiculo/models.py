from django.db import models
from crm_modelos.models import Modelos
from crm_acessorios_veiculo.models import AcessoriosVeiculo


class ConfiguracoesVeiculo(models.Model):
    descricao = models.CharField(null=True, max_length=50, verbose_name="Descrição da Configuração")
    modelo = models.ForeignKey(Modelos, on_delete=models.CASCADE, null=True, default=0, verbose_name="Produto da Configuração")
    top_cat = models.CharField(null=True, max_length=10, verbose_name="Top Cat da Configuração")
    acessorio = models.ForeignKey(AcessoriosVeiculo, on_delete=models.CASCADE, verbose_name="Acessorio da Configuração")
    status = models.BooleanField(default=True)       
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now=True)      

    class Meta:
        db_table = 'crm_configuracoes_veiculo'
        ordering = ['modelo']

    def __str__(self):
        return f'{self.modelo} - {self.top_cat}'
