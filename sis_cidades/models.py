from django.db import models


class Cidades(models.Model):
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=50)
    regiao = models.CharField(max_length=50)
    populacao = models.IntegerField(default=0)
    porte = models.CharField(max_length=30)

    class Meta:
        db_table = 'sis_cidades'
        ordering = ['municipio']                    

    def __str__(self):
        return f'{self.municipio}-{self.uf}'