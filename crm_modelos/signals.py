from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Modelos

@receiver(pre_save, sender=Modelos)
def todos_maiusculos(sender, instance, **kwargs):
    if instance.descricao:
        instance.descricao = instance.descricao.upper()
    if instance.sigla:
        instance.sigla = instance.sigla.upper()
