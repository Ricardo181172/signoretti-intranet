from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Emitentes

@receiver(pre_save, sender=Emitentes)
def todos_maiusculos(sender, instance, **kwargs):
    # Verifica se 'descricao' não é nulo antes de aplicar upper()
    if instance.nome:
        instance.nome = instance.nome.upper()
