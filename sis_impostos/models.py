from django.db import models


class Impostos(models.Model):
    descricao = models.CharField(max_length=50)
    incidencia = models.CharField(max_length=20)
    taxa = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True, verbose_name="Status do Emitente")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now=True)      

    class Meta:
        db_table = 'sis_impostos'
        ordering = ['descricao']

    def __str__(self):
        return f'{self.descricao}'