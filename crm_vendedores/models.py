from django.db import models
from sis_emitentes.models import Emitentes


class Vendedores(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Vendedor")
    sobrenome = models.CharField(max_length=150, verbose_name="Sobrenome do Vendedor")
    emitente = models.ForeignKey(Emitentes, on_delete=models.CASCADE, verbose_name="Emitente do Vendedor")
    e_mail = models.EmailField(blank=True, null=True, verbose_name="E-mail do Vendedor")
    celular = models.CharField(blank=True, null=True, max_length=20, verbose_name="Celular do Vendedor")
    usuario_crm = models.CharField(blank=True, null=True, max_length=20, verbose_name="Usuário CRM do Vendedor")
    senha_crm = models.CharField(blank=True, null=True, max_length=20, verbose_name="Senha CRM do Vendedor")
    status = models.BooleanField(default=True, verbose_name="Status do Vendedor")
    data_criacao = models.DateTimeField(null=True, auto_now_add=True, verbose_name="Data da Criação")
    data_ultima_edicao = models.DateTimeField(null=True, auto_now=True, verbose_name="Data da Ultima Edição")    

    def delete(self, using=None, keep_parents=False):
        self.status = False
        self.save()   

    class Meta:
        db_table = 'crm_vendedores'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
