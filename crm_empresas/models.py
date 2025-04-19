from django.db import models
from sis_cidades.models import Cidades


class Empresas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Empresa")
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, verbose_name="Cidade da Empresa")
    tipo_empresa = models.CharField(max_length=30, verbose_name="Tipo da Empresa")
    status = models.BooleanField(default=True, verbose_name="Status da Empresa")       
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(auto_now=True, verbose_name="Data da Ultima Edição")

    def delete(self, using=None, keep_parents=False):
        self.status = False
        self.save()      

    class Meta:
        db_table = 'crm_empresas'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome}'
