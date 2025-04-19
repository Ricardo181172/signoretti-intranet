from django.db import models
from sis_cidades.models import Cidades
from sis_emitentes.models import Emitentes
from crm_vendedores.models import Vendedores


class Clientes(models.Model):
    emitente = models.ForeignKey(Emitentes, on_delete=models.CASCADE, null=True, verbose_name="Cidade do Cliente")
    nome = models.CharField(max_length=200, verbose_name="Nome do Cliente")
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, verbose_name="Cidade do Cliente")
    vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE, default=0, verbose_name="Vendedor do Cliente")
    categoria = models.CharField(null=True, max_length=30)
    cpf_cnpj = models.CharField(max_length=50, verbose_name="CPF/CNPJ do Cliente")
    tipo_cliente = models.CharField(max_length=20, verbose_name="Tipo do Cliente")
    e_mail = models.CharField(null=True, max_length=100)
    frota_ativa = models.IntegerField(null=True, default=0)
    frota_total = models.IntegerField(null=True, default=0)
    area_plantada = models.BigIntegerField(null=True, default=0)
    indicador_temperatura = models.CharField(null=True, max_length=100)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    status_relacionamento =  models.CharField(null=True, max_length=100)
    celular = models.CharField(null=True, max_length=20)
    status = models.BooleanField(default=True, verbose_name="Status")
    data_criacao = models.DateTimeField(null=True, auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True, verbose_name="Data da Ultima Edição")    

    def delete(self, using=None, keep_parents=False):
        self.status = False
        self.save()   

    class Meta:
        db_table = 'crm_clientes'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome}'
