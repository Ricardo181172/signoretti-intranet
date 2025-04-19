from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Culturas

@receiver(pre_save, sender=Culturas)
def todos_maiusculos(sender, instance, **kwargs):
    # Verifica se 'descricao' não é nulo antes de aplicar upper()
    if instance.descricao:
        instance.descricao = instance.descricao.upper()    