from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ConfiguracoesVeiculo

@receiver(pre_save, sender=ConfiguracoesVeiculo)
def todos_maiusculos(sender, instance, **kwargs):
    if instance.descricao:
        instance.descricao = instance.descricao.upper()
    if instance.top_cat:
        instance.top_cat = instance.top_cat.upper()
