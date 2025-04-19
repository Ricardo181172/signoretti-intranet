from django.db import models


class Produtos(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição do Tipo de Equipamento")
    sigla = models.CharField(max_length=15, verbose_name="Sigla do Tipo de Equipamento")
    status = models.BooleanField(default=True, verbose_name="Status do Tipo de Equipamento")
    data_criacao = models.DateTimeField(null=True, auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True, verbose_name="Data da Ultima Edição")    

    def delete(self, using=None, keep_parents=False):
        self.status = False
        self.save()

    class Meta:
        db_table = 'crm_produtos'
        ordering = ['descricao']

    def __str__(self):
        return f'{self.descricao}'
